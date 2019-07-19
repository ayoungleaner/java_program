from scipy.spatial import distance
import redis
import scara
import time
import numpy as np
import json
import cv2
import arrow
import time
import pyzbar.pyzbar as pyzbar
  #import matplotlib.pyplot as plt
import numpy as np
corer = redis.Redis(host='localhost', port=6379, db=0)
#s = scara.Scara(True)
#400数据点
#  ros 400 

mediaposition=(400,0,0,0,'开始点')
belttest1position=(281.45,274.61,0,0,'皮带测试点1')

belttest2position=(11.45,274.61,-90,-90,'皮带测试点2')

#controlbox1position=(292.8,-256.6,-105,-105,'定夹具放')
controlbox1position=(300,-263.6,-105,-105,'定夹具放')

controlbox2position=(300,-263.6,-105,-105,'定夹具夹')

#jiaju0position=(33.57,-370.26,-78.7,-0.0,'夹具0')，r=3
#气缸歪，调整后的电源0号位置,r=-0.3
jiaju0position=(26.07,-369.26,-78.8,-78.8,'夹具0')
jiaju1position=(32.5,-345.52,-179.02,-179.02,'夹具1')
jiaju2position=(32.5,-319.48,-179.02,-179.02,'夹具2')
jiaju3position=(32.5,-293.11,-179.02,-179.02,'夹具3')

#stbpowerposition=(220.96,-281.78,-104.7,-104.7,'机顶盒电源预备插入')
stbpowerposition=(213.46,-280.58,-104.8,-104.8,'机顶盒电源预备插入')
#stbpowerpluginposition=(231.96,-281.78,-104.7,-104.7,'机顶盒电源进入点')
stbpowerpluginposition=(224.46,-280.58,-104.8,-104.8,'机顶盒电源进入点')
#cameraposition=(344,100,-6,-6,'扫码摄像机')
cameraposition=(262,97,-4,-4,'扫码摄像机')

s=None

graspstate=None
grasptool='grasp'
jiaboxstate='release'
roboticmode='700'
roboticmode='400'
def getTestposition(x,y):
        if roboticmode=='400':
                return(x*4.0/7.0,y*4.0/7.0)
        if roboticmode=='700':
                return (x,y)
        return (x,y)
def getTestarea(area):
        if roboticmode=='400':
                return(area[0]*4.0/7.0,area[1]*4.0/7.0,area[2]*4.0/7.0,area[3]*4.0/7.0)
        if roboticmode=='700':
                return area
        return area
def scarainit():
    global s

    s = scara.Scara(True)
#    s.switchManual(False)
    s.xy_max=400
    pose0=s.getPose()
#    print(pose0.x,pose0.y,pose0.z,pose0.r)

def getPose():
    pose0=s.getPose()
#    print(pose0.x,pose0.y,pose0.z,pose0.r)   
    return pose0
def mediapoint():
    print("start")
    s.moveAxis(s.axis_z,-0.02)
    s.moveXY(430,-422.45,True)
def mediapointcommon():
    print("start")
    s.moveAxis(s.axis_z,-0.02)
    x,y=getTestposition(mediaposition[0],mediaposition[1])
    s.moveXY(x,y,True)
    
def beltstartpoint():
    print("beltstart")
    s.moveAxis(s.axis_z,-0.02)
    s.moveXY(beltstartposition[0],beltstartposition[1],True)
    
def readypart():
    pose0=s.getPose()
    print(pose0.x,pose0.y,pose0.z,pose0.r)
    if pose0.z<=-0.03:
            print("tow lower")
            return 
    if pose0.r !=-180.0:
           print("r axis eror must be -180")
           return 
    jia()
    mediapoint()
    pickdown4()
def SwitchGrasp2():
    global grasptool
    
    pose0=s.getPose()
    print(pose0.x,pose0.y,pose0.z,pose0.r)
    if pose0.z<=-0.03:
        print("tow low")
        return Falsegrasprelease
#    s.moveAxis(s.axis_r,-180)
    stbfront()
    s.switchGripper(True,0.1)
    grasptool='grasp'
    time.sleep(1)

def SwitchGrasp10():
    global grasptool
    pose0=s.getPose()
    print(pose0.x,pose0.y,pose0.z,pose0.r)
    if pose0.z<=-0.03:
        print("tow low")
    s.switchGripper(False,0.1)
    time.sleep(2)
#ros 700
#    s.moveAxis(s.axis_r,-271)
#ros 400 
    s.moveAxis(s.axis_r,2.0)
    grasptool='electric'
def SwitchGrasp11():
    global grasptool
    pose0=s.getPose()
    print(pose0.x,pose0.y,pose0.z,pose0.r)
    if pose0.z<=-0.03:
        print("tow low")
#   old model
#ros 700
#    s.moveAxis(s.axis_r,-180)
#ros 400
    s.moveAxis(s.axis_r,-90)
    grasptool='electric180'
def SwitchGrasp21():
    pose0=s.getPose()
    print(pose0.x,pose0.y,pose0.z,pose0.r)
    if pose0.z<=-0.03:
        print("tow low")
    s.switchGripper(True,0.1)
    time.sleep(1)
def stbfront():
#ros700
#    s.moveAxis(s.axis_r,-180)
#ros400
    s.moveAxis(s.axis_r,-90)
    
def stbback():

#ros700
#    s.moveAxis(s.axis_r,0)
#ros 400
    s.moveAxis(s.axis_r,90)
def graspbelt():
    
#ros700
#    s.moveAxis(s.axis_r,-90)
#ros400
    s.moveAxis(s.axis_r,0)
    
def controlboxclose():
        global jiaboxstate
        
        s.controlHolder(True)
        jiaboxstate='jia'
        time.sleep(1)
def controlboxopen():
        global jiaboxstate
        s.controlHolder(False)
        jiaboxstate='release'
        time.sleep(1)
def graspjia():
    global graspstate
    s.controlGripperGrab(True,0.1)
    graspstate='jia'
def grasprelease():
    global graspstate
    s.controlGripperGrab(False,0.1) 
    graspstate='release'
def scaraspeed(newspeed):
    s.speed(newspeed)


#转换抓手
def grasptrue():
    global grasptool
    
    pose0=s.getPose()
   # print(pose0.x,pose0.y,pose0.z,pose0.r)
    if pose0.z<=-0.03:
        print("tow low")
        raise Exception ('tow low')
        #return False
	#    s.moveAxis(s.axis_r,-180)
    s.switchGripper(True,0.1)
    s.moveAxis(s.axis_r,0)
    grasptool='grasp'
    time.sleep(1)
    
def graspfalse():
    global grasptool
    pose0=s.getPose()
    #print(pose0.x,pose0.y,pose0.z,pose0.r)
    if pose0.z<=-0.03:
        print("tow low")
        raise Exception('tow low')
    s.switchGripper(False,0.1)
    time.sleep(2)
	#ros 700
	#    s.moveAxis(s.axis_r,-271)
	#ros 400 
    s.moveAxis(s.axis_r,-0.3)
    grasptool='electric'


#获取图片数据
def getVisionposition():
    cmd = corer.lpop('apriltag')
    #print(cmd)
   
    if not cmd is None:
        cmddict = json.loads(cmd)
        print(cmddict)
        return (cmddict['x'],cmddict['y'],cmddict['start'],cmddict['frametime'])
#图片数据清零
def clearVisionpositionqueue():
        while True:
                cmd = corer.lpop('apriltag')
                if cmd is None:
                    break
#归零
def gui0():
    s.moveAxis(s.axis_z,0)
    s.moveAxis(s.axis_r,0)
    s.moveXY(400.0,0.0,True)
    pose0=getPose()
    x.value=round(pose0.x,2)
    y.value=round(pose0.y,2)
    z.value=round(pose0.z,2)
    r.value = round(pose0.r,2)



#400公式
def computeposition(m,n):
    yuandian=(538.95,676.91)
    kx =1 
    ky =1
    scarax = yuandian[0] - kx*m 
    scaray = yuandian[1] - ky*n
    return (scarax,scaray)

#ros400静态抓机顶盒
def pidaijingzhua():
    clearVisionpositionqueue()
    time.sleep(10)
    ret=getVisionposition()
    if ret is None:
        print("no ret")
        raise Exception('no ret')
        #return 
    x,y,start,frametime=ret
    sx,sy=computeposition(x,y)
    print(sx,sy)
    graspbelt()
    s.moveXY(sx,sy,True)
    s.moveAxis(s.axis_z,-97)
    s.controlGripperGrab(True,0.1)
    s.moveAxis(s.axis_z,-0.02)

#ros400工作区工作
def gotoworkpalce():
    jiajufang400()
    controlboxclose()
    graspfalse()
    jia6()
    pickdown7()
    time.sleep(2)
    jia7()
    pickdown6()
    safearea()
    grasptrue()
    controlboxopen()
    jiajujia400()
    s.moveXY(400,0,True)

#ros400动态抓机顶盒
def pidaidongzhua03():
    global grapstate
    pose0=s.getPose()
    bRet= np.isclose(0.0, pose0.r, rtol=1e-03, atol=1e-03, equal_nan=False)
    if not bRet:
        #print("no 0.0")
        raise Exception('r no 0.0')
        #return 
    if graspstate!='release':
        #print("no release")
        raise Exception('graspstate no release')
    for i in range(1,300):
        ret=getVisionposition()
        if ret is None :
            #print("no ret")
            time.sleep(0.1)
            continue
        time1=time.time()
        m,n,start,frametime=ret
        if (time1-start)>10:
            #print("no right time")
            continue
        sx,sy=computeposition(m,n)
        if sx>330 and sx<480 and sy<330:
            break
    print(sx,sy)
    scarastart=time.time()
    s.moveXY(225,sy,True)
    #scaramiddle=time.time()
    s.moveAxis(s.axis_z,-97,True)
    scaraend=time.time()
    wt=(sx-225)/23.7-(scaraend-scarastart)-(time1-frametime)
    time.sleep(wt)
    graspjia()
    s.moveAxis(s.axis_z,-0.02)

#设置安全区    
def safearea():
    s.moveAxis(s.axis_z,-0.02)
    s.moveXY(300,-263.6,True)

#夹紧状态初始化
def zhuainit():
    graspjia()
    time.sleep(0.5)
    grasprelease()

#放回方法需要改善
def gotobelt():
    s.moveXY(201.45,294.61,True)
    s.moveAxis(s.axis_z,-97)
    s.controlGripperGrab(False,0.1)
    s.moveAxis(s.axis_z,-0.02)
    s.moveXY(400,0,True)

#1号位电源取出
def jia6():
    global grasptool
    if grasptool !='electric':
        print("grasp tool error")
        raise Exception('grasp tool error')
        #return 
    s.moveAxis(s.axis_z,-0.02)
    s.moveXY(jiaju0position[0],jiaju0position[1],True)
    time.sleep(0.2)
    s.moveAxis(s.axis_z,-78.8)
    time.sleep(0.2)
    s.controlGripperPlug(True,0.1)
    time.sleep(1)  
    s.moveAxis(s.axis_z,-0.02)

#1号位电源放回
def pickdown6():
    global grasptool
    if grasptool !='electric':
        print("grasp tool error")
        raise Exception('grasp tool error')
        #return 
    s.moveAxis(s.axis_z,-0.02)
    s.moveXY(jiaju0position[0],jiaju0position[1],True)
    time.sleep(0.2)
    s.moveAxis(s.axis_z,-78.8)
    time.sleep(0.2)
    s.controlGripperPlug(False,0.1)
    time.sleep(1)  
    s.moveAxis(s.axis_z,-0.02)

#电源拔出
def jia7():
    global grasptool
    if grasptool !='electric':
        print("grasp tool error")
        raise Exception('grasp tool error')
        #return 
    s.moveAxis(s.axis_z,-0.02)
    s.moveXY(stbpowerpluginposition[0],stbpowerpluginposition[1],True)
    time.sleep(0.2)
    s.moveAxis(s.axis_z,-104.8)
    time.sleep(0.2)
    s.controlGripperPlug(True,0.1)
    time.sleep(1)
    s.moveXY(stbpowerposition[0],stbpowerposition[1],True)
    s.moveAxis(s.axis_z,-0.02)

#电源插入
def pickdown7():
    global grasptool
    if grasptool !='electric':
        print("grasp tool error")
        raise Exception('grasp tool error')
        #return 
    s.moveAxis(s.axis_z,-0.02)
    s.moveXY(stbpowerposition[0],stbpowerposition[1],True)
    time.sleep(0.2)
    s.moveAxis(s.axis_z,-104.8)
    time.sleep(1)
    s.moveXY(stbpowerpluginposition[0],stbpowerpluginposition[1],True)
    time.sleep(1)
    s.controlGripperPlug(False,0.1)
    time.sleep(1)
    s.moveAxis(s.axis_z,-0.02)

#去定夹具夹机顶盒
def jiajujia400():
    global grapstate
    pose0=s.getPose()
    bRet= np.isclose(0.0, pose0.r, rtol=1e-03, atol=1e-03, equal_nan=False)
    if not bRet:
        print("no 0.0")
        raise Exception('r no 0.0')
        #return 
    if graspstate!='release':
        print("no release")
        raise EXception('graspstate no release')
        #return 
    s.moveAxis(s.axis_z,-0.02)
    s.moveXY(controlbox2position[0],controlbox2position[1],True) 
  #    time.sleep(0.1)
    s.moveAxis(s.axis_z,-105)
  #    time.sleep(0.1)
    s.controlGripperGrab(True,0.1)
  #    time.sleep(0.1)
    s.moveAxis(s.axis_z,-0.02)

#机顶盒放入定夹具
def jiajufang400():
    pose0=s.getPose()
    bRet= np.isclose(0.0, pose0.r, rtol=1e-03, atol=1e-03, equal_nan=False)
    if not bRet:
        print("no 0.0")
        raise Exception('r no 0.0')
        #return 
    s.moveAxis(s.axis_z,-0.02)
    s.moveXY(controlbox1position[0],controlbox1position[1],True)
#    time.sleep(0.1)
    s.moveAxis(s.axis_z,-105)
#    time.sleep(0.1)
    s.controlGripperGrab(False,0.1)
#    time.sleep(0.1)
    s.moveAxis(s.axis_z,-0.02)


#(400,0)位置夹
def jia400():
    #s.speed(50)
    global grapstate
    #global grasptool
    #global s
    pose0=s.getPose()
    bRet= np.isclose(-90.0, pose0.r, rtol=1e-03, atol=1e-03, equal_nan=False)
    if not bRet:
        print("no -90.0")
        raise Exception('r no 90')
        #return 
    if graspstate!='release':
        raise Exception('graspstate no release')
    #if grasptool!='grasp'
        #raise Exception('graspstool no release')
        #return 
    s.moveAxis(s.axis_z,-0.02)
    s.moveXY(mediaposition[0],mediaposition[1],True)
#    time.sleep(0.1)
    s.moveAxis(s.axis_z,-111)
#    time.sleep(0.1)
    s.controlGripperGrab(True,0.1)
#    time.sleep(0.1)
    s.moveAxis(s.axis_z,-0.02)
#（400，0）放
def pickdown400():
    pose0=s.getPose()
    bRet= np.isclose(-90.0, pose0.r, rtol=1e-03, atol=1e-03, equal_nan=False)
    if not bRet:
        print("no -90.0")
        raise Exception('r no 90')
        #return 
    s.moveAxis(s.axis_z,-0.02)
    s.moveXY(mediaposition[0],mediaposition[1],True)
#    time.sleep(0.1)
    s.moveAxis(s.axis_z,-111)
#    time.sleep(0.1)
    s.controlGripperGrab(False,0.1)
#    time.sleep(0.1)
    s.moveAxis(s.axis_z,-0.02)

#获取条形码

def capturephoto():
    cap = cv2.VideoCapture(1)
    start=time.time()
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        decoded = pyzbar.decode(gray)
        if len(decoded)==2:
            print(decoded[0][0].decode('utf-8'))
            print(decoded[1][0].decode('utf-8'))
            break
        end = time.time()
        if ( (end-start)>5):
            break
    cap.release()
    if len(decoded)!=2:
        print('wrong barcode')
    #print(decoded[0][0].decode('utf-8'))
    #print(decoded[1][0].decode('utf-8'))
#扫码

def saoma():
    global grapstate
    pose0=s.getPose()
    bRet= np.isclose(0.0, pose0.r, rtol=1e-03, atol=1e-03, equal_nan=False)
    if not bRet:
        #print("no 0.0")
        raise Exception('r no 0.0')
        #return
    s.moveAxis(s.axis_z,-0.02)
    s.moveXY(cameraposition[0],cameraposition[1],True)
    #time.sleep(0.1)
    s.moveAxis(s.axis_z,-4)
    capturephoto()
    #s.moveAxis(s.axis_z,-0.02)

#测试移动位置用
def move01():
    s.moveXY(271.45,274.61,True)
def move02():
    s.moveAxis(s.axis_z,-25)