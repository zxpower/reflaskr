# ReFlaskr

Updated version of blog app Flaskr from Python tiny MVC framework [Flask tutorial](http://flask.pocoo.org/docs/tutorial/)

_by [digiBlink](http://digiblink.eu/)_

## Installation

1.  Get it from here using [ZIPball](https://github.com/zxpower/reflaskr/zipball/master) or cloning it by git:

    `git://github.com/zxpower/reflaskr.git`

2.  Go into freshly created folder:

    `cd reflaskr/src`

3.  Create the database:

    `sqlite3 /tmp/flaskr.db < schema.sql`

4.  Run the app!

    `python app.py` or `python3 app.py`

5.  Open [http://localhost:5000/](http://localhost:5000/) in your browser to test the site. Use `admin` as username and `default` as password to login to system.
	
To run the app correctly you will require following Python prerequisites installed:
*  [`flask`](http://flask.pocoo.org/) (and all it's prerequisites)
*  [`sqlite`](http://sqlite.org/) and it's [bindings](http://wiki.python.org/moin/SQLite)

## Building and running Docker image

1.  You can run everything via [Docker](https://www.docker.com/). First you need to build the image that can be done using script provided:

    `buildImage.sh` - will produce a local image

2.  Next you need to run your newly built container using:

    `docker run --name reflaskr -d -p 8080:8080 reflaskr:latest`

3.  Now you're able to access `reflaskr` by opening [http://localhost:8080/](http://localhost:8080/).

**Note** - Docker image built is run as `non-root` user for security measures. You can use it as blueprint for creating your own Docker images for running `flask` in production. [This article](https://medium.com/@smirnov.am/running-flask-in-production-with-docker-1932c88f14d0) contains some hints on how the image is built and how it could be used or debugged.

## Support

If you run into any issues, visit [project's issue page](https://github.com/zxpower/reflaskr/issues) and report an issue.

This is free software so feel free to use it/modify it as you wish.

If you have any ideas for the next release make sure to post them [here](https://github.com/zxpower/reflaskr/issues) and mark them as `feature-request`!
