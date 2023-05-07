from machine import Pin, PWM
from time import sleep

pin = Pin("LED", Pin.OUT)
pin.on()
# pwm = PWM(Pin(0))
# pwm.freq(50)
# def setServoCycle (position):
#     pwm.duty_u16(position)
#     sleep(0.01)
# while True:
#     for pos in range(1000,9000,50):
#         setServoCycle(pos)
#     for pos in range(9000,1000,-50):
#         setServoCycle(pos)