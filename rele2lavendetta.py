import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

while True:
	GPIO.setup(7, GPIO.OUT)
	sleep(1)
	GPIO.setup(7, GPIO.IN)
	sleep(1)
