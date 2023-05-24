import utime
from servo import Servo
 
#ss = PWM(Pin(0))
#ss.freq(50)
s1 = Servo(0)       # Servo pin is connected to GP21
s2 = Servo(1)      # Servo pin is connected to GP28
s3 = Servo(2)
s4 = Servo(3)
s5 = Servo(4)
s6 = Servo(5)

s7 = Servo(7)       # Servo pin is connected to GP21
s8 = Servo(8)      # Servo pin is connected to GP28
s9 = Servo(9)
s10 = Servo(10)
s11 = Servo(11)
s12 = Servo(12) 
speed = 7

def main():
    while True:
        
        #ss.duty_u16(512)
        print("Pick Up...")
        for i in range(70, 110):
            #ss.duty_u16(0)
            servo_Angle(i, s1)
            utime.sleep_ms(speed)
                

def servo_Map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
 
def servo_Angle(angle, s):
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    s.goto(round(servo_Map(angle,0,180,0,1024))) # Convert range value to angle value
    
if __name__ == '__main__':
    main()
    
