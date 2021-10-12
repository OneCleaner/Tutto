import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)

GPIO.output(7, GPIO.HIGH)
sleep(5)
GPIO.output(7, GPIO.LOW)
sleep(5)
