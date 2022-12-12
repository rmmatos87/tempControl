# Programa : Sensor de temperatura DHT11 com Raspberry Pi
# Autor : FILIPEFLOP

# Carrega as bibliotecas
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
from datetime import datetime
from pymongo import MongoClient

uri = r"mongodb+srv://cluster0.ptnhbto.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = MongoClient(
    uri,
    tls=True,
    tlsCertificateKeyFile='cert/X509-cert.pem'
)

db = client['pi']
col_temp = db['temp']
col_umid = db['umid']

# Define o tipo de sensor
sensor = Adafruit_DHT.DHT11

GPIO.setmode(GPIO.BOARD)

# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 24
pino_relay = 23

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
    now = datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    print(now, end=" ")
    # Caso leitura esteja ok, mostra os valores na tela
    if temp is not None:
        print(f"T = %.1f °C. " % temp, end="")
        col_temp.insert_one({now: temp})
    else:
        print("Falha na leitura da temperatura. ")
    if umid is not None:
        print(f"Um = %.1f %%" % umid)
        col_umid.insert_one({now: umid})
    else:
        print("Falha na leitura da umidade.")
        time.sleep(60)