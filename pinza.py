from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
while 1:
	input()
	kit.servo[7].angle = 0
	print("0")
	input()
	kit.servo[7].angle = 180
	print("180")
