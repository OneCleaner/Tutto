from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16)
time = 1
const = time/25
grads = 3

kit.servo[4].angle = 120
#for i in range(0, 180):
#	kit.servo[2].angle = i
#	sleep(const)
while 1:
    kit.servo[6].angle = 0
    sleep(time)
    kit.servo[3].angle = 180
    sleep(time)
    #for i in range(120, 100, grads * -1):
    #    kit.servo[4].angle = i
    #    sleep(const)
    #sleep(time)
    for i in range(0, 100, grads):
        kit.servo[0].angle = i
        sleep(const)
    sleep(time)
    for i in range(100, 171, grads):
        kit.servo[0].angle = i
        sleep(const)
    sleep(time)
    kit.servo[1].angle = 100
    sleep(time)
    kit.servo[6].angle = 100
    sleep(time)
    for i in range(161, -1, grads * -1):
        kit.servo[0].angle = i
        sleep(const)
    sleep(time)
    #for i in range(50, 110, grads):
    #    kit.servo[4].angle = i
    #    sleep(const)
    sleep(time)
    kit.servo[1].angle = 10
    sleep(time)
    kit.servo[3].angle = 130
    sleep(time)
    kit.servo[6].angle = 0
