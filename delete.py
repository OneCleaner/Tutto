from adafruit_servokit import ServoKit
from time import sleep
from pygame.joystick import Joystick
from pygame import init, JOYBUTTONDOWN
from pygame.event import get

init()
kit = ServoKit(channels=16)
joystick = Joystick(0)
joystick.init()
axes = joystick.get_numaxes()
i = 60

kit.servo[2].angle = 0

while True:
       while i < 100:
               i+= 1
               kit.servo[2].angle = i
               sleep(0.1)
       while i > 0:
               i -= 1
               kit.servo[2].angle = i
               sleep(0.1)
#debug = 1
#while 1:
#    events = get()
#    for lvr in range(axes):
#        axis = joystick.get_axis(lvr)
#        if lvr == 2:
#            if axis > 0.50:
#                if debug == 1:
#                    print("Ruota a destra")
#                if i > 5 and i < 175:
#                    i += 2
#                    kit.servo[2].angle = i
#            elif axis < -0.50:
#                if debug == 1:
#                    print("Ruota a sinistra")
#                if i > 5 and i < 175:
#                    i -= 1
#                    kit.servo[2].angle = i
#        if lvr == 4:
#            if axis > 0.50:
#                if debug == 1:
#                    print("Apri la pinza")
#                i += 1
#                kit.servo[0].angle = i
#        if lvr == 5:
#            if axis > 0.50:
#                if debug == 1:
#                    print("Chiudi la pinza")
#                i -= 1
#                kit.servo[0].angle = i

