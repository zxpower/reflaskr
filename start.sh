#!/usr/bin/env bash
sqlite3 /tmp/flaskr.db < src/schema.sql
service nginx start
uwsgi --ini uwsgi.ini
