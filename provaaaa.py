"""test server"""
from socket import socket, AF_INET, SOCK_STREAM, gethostbyname, gethostname
from serial import Serial
from adafruit_servokit import ServoKit

#ARDUINO_PORT = input("Arduino Port: ")
#SERIAL_PORT = Serial(ARDUINO_PORT, 9600)
#SERIAL_PORT.flushInput()
ANGLE = [0] * 5
KIT = ServoKit(channels=16)
SOCK = socket(AF_INET, SOCK_STREAM)
HOST = gethostbyname(gethostname())
print(HOST)
SOCK.bind(("172.20.10.9", 7503))
SOCK.listen(1)
CONN, ADDR = SOCK.accept()
print(ADDR)
while True:
    COMMAND = CONN.recv(512)
    if COMMAND == b"ap0":
        ANGLE[0] += 1
    elif COMMAND == b"cp0":
        ANGLE[0] -= 1
    elif COMMAND == b"ms1":
        ANGLE[1] += 1
    elif COMMAND == b"md1":
        ANGLE[1] -= 1
    elif COMMAND == b"cs1":
        ANGLE[1] += 1
    elif COMMAND == b"cd1":
        ANGLE[1] -= 1
   # else:
	#print("123")
        #SERIAL_PORT.write(COMMAND)
    for i in range(0, 5):
        KIT.servo[i].angle = ANGLE[i]
    KIT.servo[0].angle = 180

