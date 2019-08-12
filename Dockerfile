FROM python:3.7-slim-stretch

RUN mkdir /app; chown -R 1000:1000 /app;
WORKDIR /app

COPY configs/requirements.txt /app/requirements.txt

RUN apt-get update; \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends gcc make libc6-dev libpq-dev nginx sqlite3; \
    dpkg -L binutils | grep -v  "^/usr/bin\|^/usr/lib" | while read f; do test -f $f && rm $f; done; \
    dpkg -L gcc-6    | grep -v  "^/usr/bin\|^/usr/lib" | while read f; do test -f $f && rm $f; done; \
    apt-get autoremove -y; apt-get clean; rm /var/lib/apt/lists/* -r; rm -rf /usr/share/man/*; \
    pip3 install --no-cache -r /app/requirements.txt; \
    echo 'export TERM="xterm"' >> /app/.bashrc; \
    apt-get clean; \
    addgroup --system --gid 1000 app; \
    adduser --system --home /app --disabled-password --uid 1000 --gid 1000 app; \
    mkdir -p /var/cache/nginx;

ENV PYTHONPATH /app
COPY ./src /app/src

COPY configs/nginx.conf /etc/nginx
COPY configs/uwsgi.ini /app
COPY start.sh /app
RUN chmod +x /app/start.sh; \
    chown -R 1000:1000 /app; \
    chown -R 1000:0 /var/cache/nginx; \
    chown -R 1000:1000 /var/www/html; \
    chown -R 1000:adm /var/log/nginx;

EXPOSE 8080

USER 1000

CMD ["./start.sh"]

