import RPi.GPIO as gpio
from time import time, sleep
d = 6
a = 12

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(d, gpio.OUT)
gpio.setup(a, gpio.OUT)
gpio.output(d, gpio.HIGH)
gpio.output(a, gpio.HIGH)
gpio.setup(16, gpio.IN, gpio.PUD_DOWN)

on = False

#x = input("(b)utton or (k)eyboard? ")
#if x == 'b':
#   while 1:
#       print("started")
#       if gpio.input(16) == gpio.HIGH:
#           if on:
#               print("pressed")
#               on = False
#               gpio.output(d, gpio.HIGH)
#               gpio.output(a, gpio.LOW)
#           else:
#               gpio.output(a, gpio.HIGH)
#               gpio.output(d, gpio.LOW)
#               on = True
#   #sleep(0.5)
#elif x == 'k':
#   while 1:
#       input()
#       gpio.output(d, gpio.HIGH)
#       gpio.output(a, gpio.LOW)
#       input()
#       gpio.output(a, gpio.HIGH)
#       gpio.output(d, gpio.LOW)
#
input()
print("Button check")
while gpio.input(16) != gpio.HIGH:
    pass
print("Check 1 OK")
sleep(2)
while gpio.input(16) != gpio.HIGH:
    pass
print("Check 2 OK")
input()
input()
input()
#start = time()
gpio.output(d, gpio.LOW) #chiudi
gpio.output(a, gpio.HIGH)
sleep(1)
gpio.output(d, gpio.LOW) #ferma
gpio.output(a, gpio.LOW)
sleep(1)
from sys import exit as sysexit
sysexit()
while gpio.input(16) == gpio.LOW:
    pass
#end = time()
#closetime = end - start
sleep(0.9)
gpio.output(d, gpio.LOW) #ferma
gpio.output(a, gpio.LOW)
input()
gpio.output(d, gpio.HIGH) #apri
gpio.output(a, gpio.LOW)
#sleep(closetime)
sleep(2.5)
gpio.output(d, gpio.LOW) #ferma
gpio.output(a, gpio.LOW)
