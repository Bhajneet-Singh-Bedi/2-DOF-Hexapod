import utime
from servo import Servo
 
s1 = Servo(21)       # Servo pin is connected to GP21
s2 = Servo(28)      # Servo pin is connected to GP28

speed = 5

def main():
    while True:
        
        print("Pick Up ...")
        for i in range(30, 120):
            servo_Angle(i, s1)
            utime.sleep_ms(speed)
        print("Turn Left ...")
        for i in range(50, 120):
            servo_Angle(i, s2)
            utime.sleep_ms(speed)
        print("Go Down ...")
        for i in range(120, 30, -1):
            servo_Angle(i, s1)
            utime.sleep_ms(speed)
        print("Turn Right ...")
        for i in range(120, 50, -1):
            servo_Angle(i, s2)
            utime.sleep_ms(speed)
        
        """
        print("Pick Up ...")
        for i in range(0, 90):
            servo_Angle(i, s2)
            utime.sleep_ms(8)
        print("Go Down ...")
        for i in range(90, 0):
            servo_Angle(i, s2)
            utime.sleep_ms(8)
        print("Turn left ...")
        for i in range(50,130,1):
            servo_Angle(i, s1)
            utime.sleep_ms(8)
        print("Turn right ...")
        for i in range(130,50,-1):
            servo_Angle(i, s1)
            utime.sleep_ms(8)
            """




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
    
