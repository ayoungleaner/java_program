#获取条形码
import cv2
import arrow
import time
import pyzbar.pyzbar as pyzbar
  #import matplotlib.pyplot as plt
import numpy as np
from ros400function import s
import ros400coordinate

def capturephoto():
    cap = cv2.VideoCapture(2)
    ret, frame = cap.read()
    filename="/home/aadebugergf/aixgf/tzimagedata/barcode/object{0}.jpg".format(arrow.now().format('YYYYMMDDHHmmss'))
    start=time.time()
    while True:
        ret, frame = cap.read()
        end = time.time()
        if ( (end-start)>5):
                break
    print(filename)   
    ret, frame = cap.read()
    cv2.imwrite(filename,frame)
    cap.release()
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  #    plt.imshow(gray, cmap='gray')
    decoded = pyzbar.decode(gray)
    print(decoded[0][0].decode('utf-8'))
    print(decoded[1][0].decode('utf-8'))

#扫码

def saoma():
    global grapstate
    pose0=s.getPose()
    bRet= np.isclose(0.0, pose0.r, rtol=1e-03, atol=1e-03, equal_nan=False)
    if not bRet:
        print("no 0.0")
        raise Exception('r no 0.0')
        #return
    s.moveAxis(s.axis_z,-0.02)
    s.moveXY(cameraposition[0],cameraposition[1],True)
    #time.sleep(0.1)
    s.moveAxis(s.axis_z,-7)
    capturephoto()
    time.sleep(2)
    #s.moveAxis(s.axis_z,-0.02)


