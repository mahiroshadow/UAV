import cv2
import subprocess
from ultralytics import YOLO


src = "rtmp://192.168.5.5:1935/live/home"
dest = "rtmp://47.98.33.192:1935/live/test"
command = [
    'ffmpeg', '-y', '-f', 'rawvideo', '-vcodec', 'rawvideo', '-pix_fmt',
    'bgr24', '-s', "{}x{}".format(720, 1280), '-r',
    str(30), '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset',
    'ultrafast', '-f', 'flv', dest
]
model = YOLO("yolo11n.pt").cuda()
cap = cv2.VideoCapture(src)
pipe = subprocess.Popen(command, shell=False, stdin=subprocess.PIPE)
while True:
    _, frame = cap.read()
    res = model(frame)[0]
    pipe.stdin.write(res.mask)
    cv2.waitKey(1)
