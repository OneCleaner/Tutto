from time import sleep, time

from RPi.GPIO import setmode, setup, output, BCM, HIGH, LOW, IN, OUT, PUD_DOWN
from RPi.GPIO import input as gpio_input
from adafruit_servokit import ServoKit

from universal import move

setmode(BCM)

POSIZIONI = {
    1: 80,
    15: 0,
    8: 20,
    3: 30
}

KIT = ServoKit(channels=16)
# PATH = "/dev/ttyUSB0"


def braccio_raw(servo, angolo):
	"""Modifica l'angolo di un servo senza delay"""
    KIT.servo[servo].angle = angolo


def braccio(servo, angolo):
	"""Modifica l'angolo di un servo con delay"""
    for i in range(POSIZIONI[servo], angolo, -1 if angolo < POSIZIONI[servo] else 1):
        braccio_raw(servo, i)
        sleep(0.02)
    POSIZIONI[servo] = angolo

# def pinza(apri, chiudi):
#	gpio.output(12, apri)
#	gpio.output(6, chiudi)


braccio_raw(1, 80)

if __name__ == "__main__":
    while True:
        srv = int(input("Servo: "))
        agl = int(input("Angolo: "))
        braccio(srv, agl)


class Pinza():
    def __init__(self) -> None:
        setup(6, OUT)
        setup(16, IN, PUD_DOWN)
        setup(12, OUT)
        self.tempo_chiusura: int

    def apri(self) -> None:
        """Apre la pinza"""
        output(12, HIGH)
        output(6, LOW)
        self.tempo_chiusura = time()

    def chiudi(self) -> None:
        """Chiude la pinza"""
        output(12, LOW)
        output(6, HIGH)
        # TODO TEST
        # sleep(self.tempo_chiusura)
        # self.stop()

    def stop(self) -> None:
        """Ferma la pinza"""
        output(12, LOW)
        output(6, LOW)
        self.tempo_chiusura = time() - self.tempo_chiusura

    def pulsante_premuto(self) -> None:
        while gpio_input(16) != HIGH:
            pass
