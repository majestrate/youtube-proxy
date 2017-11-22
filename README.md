caching youtube proxy using youtube-dl flask and celery

requires:

* python 3.6 or higher
* nginx
* redis-server

setup:

    python3 -m venv v
    ./v/bin/pip install -r requirements.txt
    
run worker:
    
    ./v/bin/celery -A youtube worker

run webapp:

    ./v/bin/gunicorn proxyserver:app -b 127.0.0.1:5000


to deploy use the provided nginx config file ``conf/nginx/youtube-proxy``

    cp conf/nginx/youtube-proxy /etc/nginx/sites-available/
    ln -s /etc/nginx/sites-available/youtube-proxy /etc/nginx/sites-enabled/

TODO:

* supervise scripts
* optionally stream live stream videos
