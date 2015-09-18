caching youtube proxy using youtube-dl flask and celery

requires:

* python 3.3 or higher
* pyvenv
* nginx
* redis-server

to use:

    # this will set up a virtual environment at venv, install dependancies into venv and start the required daemons
    ./run.sh

to deploy use the provided nginx config file ``conf/nginx/youtube-proxy``

    cp conf/nginx/youtube-proxy /etc/nginx/sites-available/
    ln -s /etc/nginx/sites-available/youtube-proxy /etc/nginx/sites-enabled/

TODO:

* supervise scripts
* optionally stream live stream videos
