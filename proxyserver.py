from flask import Flask, abort, redirect, render_template
from werkzeug.contrib.fixers import ProxyFix
import os, sys
import youtube

app = Flask(__name__)

@app.route('/video/<video_id>')
def get_youtube(video_id):
    fname = os.path.join(os.path.dirname('.'),'static','%s.mp4' % video_id)
    if '..' in video_id:
        abort(404)
    if len(video_id) == 11:
        if os.path.exists(fname+".part"):
            return render_template("progress.html", message="is downloading...", video_id=video_id)
        elif not os.path.exists(fname):
            youtube.download.apply_async((video_id, fname))
            return render_template("progress.html", message="has started", video_id=video_id)
    else:
        abort(404)
    return redirect('/yt/static/{}.mp4'.format(video_id))

@app.route('/')
def get_index():
    return render_template("index.html")

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()
