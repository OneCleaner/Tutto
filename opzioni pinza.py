import RPi.GPIO as gpio
from time import time, sleep
d = 6
a = 12

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(d, gpio.OUT)
gpio.setup(a, gpio.OUT)
#gpio.output(d, gpio.HIGH) #SI CHIUDE
#gpio.output(a, gpio.LOW)

gpio.output(d, gpio.LOW)   #SI FERMA
gpio.output(a, gpio.LOW)

#gpio.output(d, gpio.LOW) #SI APRE
#gpio.output(a, gpio.HIGH)


gpio.setup(16, gpio.IN, gpio.PUD_DOWN)
