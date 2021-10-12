from universal import move
from time import sleep
from adafruit_servokit import ServoKit
import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setup(12, gpio.OUT)
gpio.setup(6, gpio.OUT)

POSIZIONI = {
	1 : 80,
	15: 0,
	8: 20,
	3: 30
}

KIT = ServoKit(channels=16)
#PATH = "/dev/ttyUSB0"

def braccio_raw(servo, angolo):
	KIT.servo[servo].angle = angolo

def braccio(servo, angolo):
	for i in range(POSIZIONI[servo], angolo, -1 if angolo < POSIZIONI[servo] else 1):
		braccio_raw(servo, i)
		sleep(0.02)
	POSIZIONI[servo] = angolo

def pinza(apri, chiudi):
	gpio.output(12, apri)
	gpio.output(6, chiudi)

braccio_raw(1, 80)

if __name__ == "__main__":
	while True:
		srv = int(input("Servo: "))
		agl = int(input("Angolo: "))
		braccio(srv, agl)

