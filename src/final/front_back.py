from machine import Pin
from servo import Servo
import socket
import network
import utime
import gc

speed = 7
ctr=1
s1=Servo(0)
s2=Servo(1)
s3=Servo(2)
s4=Servo(3)
s5=Servo(4)
s6=Servo(5)

s7=Servo(7)
s8=Servo(8)
s9=Servo(9)
s10=Servo(10)
s11=Servo(11)
s12=Servo(12)

led = Pin("LED", Pin.OUT)
led.on()


def initial():
    servo_Angle(90, s2)
    servo_Angle(90, s6)
    servo_Angle(90, s10)
    servo_Angle(130, s12)
    servo_Angle(50, s4)
    servo_Angle(50, s8)
    ctr+=1

def front():
    # To go front.
    """
    lalla lalla lorry dudh ki katori.
    Initial comment:
        8, 4 -> 50
        12 -> 130
        2, 10, 12 -> willl come from 130 to 90
        4, 6, 8 -> will come from 50 to 90
        
    Logic wale comment:
        Pick Up, 1, 5, 9 Move them forward 6, 2, 10 and bring back 8, 12, 4.
        Pick up 7, 3, 11, then move 8, 12, 4 forward simulll... bring back 6, 2, 10. repeat the process.
    """
    """
    Go 6th front, same time 10 and 2nd.
    """
    #pickLeg3(s5, s1, s9)
    #motion1(s6, s2, s10, s8, s12, s4)
    #putLeg3(s1, s5, s9)
    #motion2(s8, s12, s4, s6, s2, s10)
    
    
    
    """
    # Go forward
    pickLeg3(s5, s1, s9)
    for i in range(90, 49, -1):
        servo_Angle(i, s6)
        servo_Angle(90+(90-i), s2)
        servo_Angle(90+(90-i), s10)
        utime.sleep_ms(speed)
    putLeg3(s5, s1, s9)
    # Come back
    for i in range(50, 91):
        servo_Angle(i, s6)
        servo_Angle(130-(i-50), s2)
        servo_Angle(130-(i-50), s10)
        utime.sleep_ms(speed)
    """
    
    ############# Right moving...
    #1, 8,,,,,4, 10,,,,,6, 12
    """
    pickLeg3(s5, s9, s1)
    for i in range(90, 59, -1):
        servo_Angle(i, s6)
        #servo_Angle(120-(90-i), s12) # -> bring from 130 to 90
        servo_Angle(i, s2)
        #servo_Angle(60+(90-i), s8) # -> bring from 50 to 90
        servo_Angle(i, s10)
        #servo_Angle(60+(90-i), s4) # -> bring from 50 to 90
        utime.sleep_ms(speed)
    putLeg3(s5, s9, s1)
    pickLeg3(s11, s3, s7)
    # Come back
    for i in range(60, 91):
        servo_Angle(i, s6)
        #servo_Angle(90+(i-60),s12) # -> bring from 90 to 130
        servo_Angle(i, s2)
        #servo_Angle(90-(i-60),s8) # -> bring from 90 to 50
        servo_Angle(i, s10)
        #servo_Angle(90-(i-60), s4) # -> bring fromm 90 to 50
        utime.sleep_ms(speed)
    putLeg3(s11, s3, s7)
    """
    ############# Right moving...
    
    
    
    
    ############# Left moving...
    """
    pickLeg3(s11, s7, s3)
    for i in range(90, 121 ):
        servo_Angle(i, s12)
        servo_Angle(i, s8)
        servo_Angle(i, s4)
        utime.sleep_ms(speed)
    putLeg3(s11, s7, s3)
    pickLeg3(s5, s9, s1)
    # Come back
    for i in range(120, 89, -1):
        servo_Angle(i, s12)
        servo_Angle(i, s8)
        servo_Angle(i, s4)
        utime.sleep_ms(speed)
    putLeg3(s5, s9, s1)
    """
    ############# Left moving...
    
    
    
    ############# Forward moving...
    """
    # Go forward
    pickLeg3(s5, s9, s1)
    for i in range(90, 59, -1):	
        servo_Angle(i, s6)
        servo_Angle(120-(90-i), s12) # -> bring from 130 to 90
        servo_Angle(90+(90-i), s2)
        servo_Angle(60+(90-i), s8) # -> bring from 50 to 90
        servo_Angle(90+(90-i), s10)
        servo_Angle(60+(90-i), s4) # -> bring from 50 to 90
        utime.sleep_ms(speed)
    putLeg3(s5, s9, s1)
    pickLeg3(s11, s3, s7)
    # Come back
    for i in range(60, 91):
        servo_Angle(i, s6)
        servo_Angle(90+(i-60),s12) # -> bring from 90 to 130
        servo_Angle(120-(i-60), s2)
        servo_Angle(90-(i-60),s8) # -> bring from 90 to 50
        servo_Angle(120-(i-60), s10)
        servo_Angle(90-(i-60), s4) # -> bring fromm 90 to 50
        utime.sleep_ms(speed)
    putLeg3(s11, s3, s7)
    """
    ######### Forward moving...
    
    """
    for i in range(90, 50, -1):
        servo_Angle(i, s6)
        utime.sleep_ms(1)
        servo_Angle(90+(90-i), s2)
        utime.sleep_ms(1)
        servo_Angle(90+(90-i), s10)
        utime.sleep_ms(speed)
    """
    
def pickLeg3(servo1, servo2, servo3):
    for i in range(90, 40, -1):
        servo_Angle(i, servo1)
        servo_Angle(i, servo2)
        servo_Angle(i, servo3)
        utime.sleep_ms(speed)
        
def putLeg3(servo1, servo2, servo3):
    for i in range(40, 90):
        servo_Angle(i, servo1)
        servo_Angle(i, servo2)
        servo_Angle(i, servo3)
        utime.sleep_ms(speed)
        
"""
def motion1(s6, s2, s10, s8, s12, s4):
    # Pick Up, 1, 5, 9 Move them forward 6, 2, 10 and bring back 8, 12, 4.
    # 6, 2, 10 are at 90 bring them to 
    # 8, 12, 4 is in 130 position (Hopefully). Bring this from 130 to 90
    # 1, 5, 9 is up. move 6, 2, 10 forward and 8 12 4 back.
    for i in range(90, 49, -1):
        servo_Angle(i, s6) # now they are forward
        #servo_Angle(50+(90-i), s8) # bring them to 90 from 50
        servo_Angle(90+(90-i), s2) #fd
        #servo_Angle(130-(90-i), s12) # bring them to 90 from 130
        servo_Angle(90+(90-i), s10) #fd
        #servo_Angle(50+(90-i), s4) # bring them to 90 from 50
        utime.sleep_ms(speed)
        
 """   
"""
def motion2(s8, s12, s4, s6, s2, s10):
    pass
    # Bring 8, 12, 4 to forward and other backward
    for i in range(50, 91):
        servo_Angle(i, s8) 
        servo_Angle(, s6) # bring them to 90 from 50
        servo_Angle(90+(90-i), s12) #fd
        servo_Angle(130-(90-i), s2) # bring them to 90 from 130
        servo_Angle(i, s4) #fd
        servo_Angle(50+(90-i), s10) # bring them to 90 from 50
        utime.sleep_ms(speed)
"""


def pickLeg2():
    pass

def putLeg2():
    pass

def moveLeg2():
    pass


def servo_Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
def servo_Angle(angle, s):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    s.goto(round(servo_Map(angle,0,180,0,1024))) # Convert range value to angle value

while True:
    front()
