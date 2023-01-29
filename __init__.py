# Programa : Sensor de temperatura DHT11 com Raspberry Pi
# Autor : FILIPEFLOP

# Carrega as bibliotecas
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
from datetime import datetime
import os
import db
import local

backup_dia = False
def backup():
    now = datetime.now().isoformat()
    os.system(r"cd /home/pi/Desktop/piProject/tempControl")
    os.system("git add .")
    os.system(f"git commit -m Backup_{now}")
    os.system("git push")
    
# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BOARD)

# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 24
pino_relay = 23

sleep = 60

GPIO.setup(pino_relay, GPIO.OUT) # GPIO Assign mode

# Informacoes iniciais
print("*** Lendo os valores de temperatura e umidade")

while(True):
    # Efetua a leitura do sensor
    umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor)
    # print(GPIO.input(pino_relay))
    # if GPIO.input(pino_relay) == GPIO.HIGH:
    #     GPIO.output(pino_relay, GPIO.LOW) # out
    # else:
    #     GPIO.output(pino_relay, GPIO.HIGH) # on
    now = datetime.now()
    print(now.isoformat(), end=" ")
    # Caso leitura esteja ok, mostra os valores na tela
    if temp is not None:
        print(f"T = %.1f °C. " % temp, end="")
    else:
        print("Falha na leitura da temperatura. ")
        temp = -1
    if umid is not None:
        print(f"Um = %.1f %%" % umid)
    else:
        print("Falha na leitura da umidade.")
        umid = -1
    try:
        ok = db.insert_measures(now, temp, umid)
        if not ok:
            local.save(now, temp, umid)
    except Exception as e:
        print(e)

    if now.hour == 12 and not backup_dia:
        backup()
        backup_dia = True
    if now.hour == 0:
        backup_dia = False
    
    time.sleep(sleep)
