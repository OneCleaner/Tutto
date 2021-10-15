from braccio_lib import braccio, Pinza
import RPi.GPIO as gpio
from time import sleep
from universal import move, s
from threading import Thread

P = Pinza()

# 1 secondo = 0,74M

#metri = input("METRI: ")
#tempo = metri / 0.74


cont = 0
RUN = True


def read():
    while RUN:
        print("ARDUINO: " + s.readline().decode())


Thread(target=read).start()

#input("PREMI INVIO PER PINZA")
P.apri()
sleep(2.5)
P.stop()

input("PREMI INVIO PER MOTORI")
move("dritto", 0)
sleep(2)
move("spegni", 0)
sleep(0.5)

# exit()

try:
    while 1:
        braccio(1, 170)

        P.chiudi()
        P.pulsante_premuto()
        sleep(0.4)
        P.stop()

        if False:  # input("MATERIALE: ") == 'p':
            # PLASTICA
            braccio(1, 40)
            braccio(3, 0)
            braccio(15, 70)
            braccio(8, 100)
            cont = 1
        else:
            # CARTA
            braccio(1, 40)
            braccio(3, 60)
            braccio(15, 70)
            braccio(8, 100)
            cont = 0

        P.apri()
        sleep(2.5)
        P.stop()

        # RESET
        braccio(15, 0)
        braccio(8, 20)
        braccio(3, 30)

        print("PREMI INVIO PER RIAVVIARE")
        input()
except KeyboardInterrupt:
    RUN = False

sleep(2)
print("END")
