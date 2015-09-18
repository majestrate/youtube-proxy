#!/bin/bash
set -e
set -x

# set these to go over a proxy
#
# export http_proxy=127.0.0.1:8118
# export https_proxy=127.0.0.1:8118

cd $(dirname $0)
mkdir -p static
if [ ! -e venv ] ; then
  pyvenv venv
fi
source venv/bin/activate
pip install -r requirements.txt
celery -A youtube worker &> worker.log &
gunicorn proxyserver:app -b 127.0.0.1:5000 &> http.log &
