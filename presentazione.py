from adafruit_servokit import ServoKit
from time import sleep
import RPi.GPIO as gpio

a = 12
d = 6

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(d, gpio.OUT)
gpio.setup(a, gpio.OUT)
gpio.setup(16, gpio.IN, gpio.PUD_DOWN)
gpio.output(d, gpio.LOW)
gpio.output(a, gpio.LOW)



kit = ServoKit(channels=16)
const = 2


def coso(min = 0, max = 180, step = 1, servo = 3, const = 1/40):
    for i in range(min, max, step):
        kit.servo[servo].angle = i
        sleep(0.02)
    #pass
while 1:
    try:
        sleep(const)
        gpio.output(d, gpio.LOW) #SI APRE
        gpio.output(a, gpio.HIGH)
        sleep(1.6)
        gpio.output(d, gpio.LOW)   #SI FERMA
        gpio.output(a, gpio.LOW)
        print("Base")
        coso(100, 40, -1, 3)
        print("altezza")
        coso(50, 150, 1, 1)
        sleep(const)
        print("altezza parte finale")
        coso(50, 0, -1, 15) #60 -> 50
        sleep(const)
        print("altezza pinza")
        coso(130, 0, -1, 8)
        sleep(const)
        gpio.output(d, gpio.HIGH) #SI CHIUDE
        gpio.output(a, gpio.LOW)
        while gpio.input(16) != gpio.HIGH:
            pass
        sleep(0.3)
        gpio.output(d, gpio.LOW)   #SI FERMA
        gpio.output(a, gpio.LOW)
        print("altezza pinza")
        coso(0, 100, 1, 8)
        sleep(const)
        print("altezza")
        coso(150, 50, -1, 1)
        sleep(const)
        print("altezza parte finale")
        coso(0, 50, 1, 15)
        sleep(const)
        print("Base")
        coso(40, 100, 1, 3)
        sleep(const)
    except KeyboardInterrupt:
        gpio.output(d, gpio.LOW)   #SI FERMA
        gpio.output(a, gpio.LOW)
        break
