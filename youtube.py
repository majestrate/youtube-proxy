import os, sys
import youtube_dl
from celery import Celery


app = Celery('youtube-proxy', broker='redis://localhost:6379/0')


@app.task
def download(video_id, fname):
    with youtube_dl.YoutubeDL({'outtmpl': fname, 'cachedir':'/tmp/youtubedl'}) as dl:
        dl.download(['https://www.youtube.com/watch?v={}'.format(video_id)])

