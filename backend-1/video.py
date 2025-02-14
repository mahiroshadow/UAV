import cv2
import json
import flask
import subprocess
from flask_cors import CORS
from ultralytics import YOLO
from flask_sockets import Sockets
import ultralytics.engine.results
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
'''
input.flv 1920x1080
golbal
'''
app = flask.Flask(__name__)
sockets = Sockets(app)
CORS(app)
model = YOLO("visdrone_l.pt").cuda()


@sockets.route('/info')
def streaming(ws):
    src = "rtmp://47.98.33.192:1936/live/stream"
    dest = "rtmp://47.98.33.192:1935/live/test"
    command = [
        'ffmpeg', '-y', '-f', 'rawvideo', '-vcodec', 'rawvideo', '-pix_fmt',
        'bgr24', '-s', "{}x{}".format(1280, 720), '-r',
        str(30), '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
        '-preset', 'ultrafast', '-f', 'flv', dest
    ]
    cap = cv2.VideoCapture(src)
    pipe = subprocess.Popen(command, shell=False, stdin=subprocess.PIPE)
    while True:
        _, frame = cap.read()
        res = model(frame)[0]
        show_info = json.loads(res.to_json())
        ws.send(show_info)
        res_frame = res.show()
        pipe.stdin.write(res_frame)
        cv2.waitKey(1)


def test(model: YOLO):
    frame = cv2.imread("slice.png")
    res: ultralytics.engine.results.Results = model(frame)[0]
    res_frame = res.show()
    cv2.imshow('image', res_frame)
    cv2.waitKey(0)


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 8888),
                               app,
                               handler_class=WebSocketHandler)
    server.serve_forever()
