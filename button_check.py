import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(16, gpio.IN, gpio.PUD_DOWN)
times = 0

while 1:
	while gpio.input(16) != gpio.HIGH:
		pass
	times += 1
	print("\rPressed " + str(times) + " times", end="\r")
	sleep(0.5)
