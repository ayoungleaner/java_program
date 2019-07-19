from scipy.spatial import distance
import redis
import scara
import time
import numpy as np
import json
import ros400coordinate
corer = redis.Redis(host='localhost', port=6379, db=0)
#s = scara.Scara(True)

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
        return False
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
    s.moveAxis(s.axis_r,2.0)
    grasptool='electric'


#获取图片数据
def getVisionposition():
    cmd = corer.lpop('apriltag')
    print(cmd)
   
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
