from adafruit_servokit import ServoKit
from time import sleep
from serial import Serial

#kit = ServoKit(channels=16)

OFF : bytes = "spegni".encode()
ON : bytes = "accendi".encode()
s = Serial("/dev/ttyUSB0", 115200)
#s.write(OFF)
command = ''
#s.write(ON)

def move(local_command, time):
	#s.write(ON)
	#sleep(2)
	s.write(local_command.encode())
	#sleep(time)
	#s.write(OFF)

if __name__ == "__main__":
	while command != 'q':
		command = input("Comando: ")
		if command in ["dritto", "destra", "sinistra", "gira-sinistra", "gira-destra", "retro", "spegni", "accendi"]:
			move(command, 1)
		else:
			s.write(OFF)
