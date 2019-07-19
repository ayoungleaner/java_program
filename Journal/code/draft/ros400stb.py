import numpy as np
import time
import ros400function
import ros400coordinate
from ros400function import s
from ros400function import grasptool
from ros400function import graspstate


#400公式
def computeposition(m,n):
    yuandian=(538.95,680.91)
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
    time.sleep(0.5)
    controlboxclose()
    time.sleep(0.5)
    graspfalse()
    jia6()
    time.sleep(0.5)
    pickdown7()
    time.sleep(2)
    jia7()
    pickdown6()
    time.sleep(0.5)
    safearea()
    time.sleep(1)
    grasptrue()
    controlboxopen()
    time.sleep(0.5)
    jiajujia400()
    s.moveXY(400,0,True)

#ros400动态抓机顶盒
def pidaidongzhua03():
    for i in range(1,15):
        ret=getVisionposition()
        if ret is None :
            print("no ret")
            time.sleep(1)
            continue
        time1=time.time()
        m,n,start,frametime=ret
        if (time1-start)>10:
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
    wt=(sx-225)/17-(scaraend-scarastart)-(time1-frametime)
    time.sleep(wt)
    graspjia()
    s.moveAxis(s.axis_z,-0.02)

#设置安全区    
def safearea():
    s.moveAxis(s.axis_z,-0.02)
    s.moveXY(300,-263.6,True)





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
    s.moveAxis(s.axis_z,-78.7)
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
    s.moveAxis(s.axis_z,-78.7)
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
    s.moveAxis(s.axis_z,-104.7)
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
    s.moveAxis(s.axis_z,-104.7)
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

#机顶盒放入定夹具jiaboxstate
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
    #global s
    pose0=s.getPose()
    bRet= np.isclose(-90.0, pose0.r, rtol=1e-03, atol=1e-03, equal_nan=False)
    if not bRet:
        print("no -90.0")
        raise Exception('r no 90')
        #return 
    if graspstate!='release':
        raise Exception('graspstate no release')
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

