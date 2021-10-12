import socket
import numpy as np
import pickle
import struct ## new
import cv2

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.103", 5007))
connection = s.makefile('wb')

cam = cv2.VideoCapture(0)

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

cam.set(3, 320);
cam.set(4, 240);

img_counter = 0

while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
    data = pickle.dumps(frame, 0)
    size = len(data)

    print("{}: {}".format(img_counter, size))
    s.sendall(struct.pack(">L", size) + data)
    img_counter += 1
