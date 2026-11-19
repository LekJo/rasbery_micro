import Adafruit_DHT
import time

SENSOR = Adafruit_DHT.DHT11
PIN = 4 # GPIO 4

print("Membaca Sensor DHT11 (Tekan Ctrl+C untuk berhenti)")
try:
    while True:
        kelembapan, suhu = Adafruit_DHT.read_retry(SENSOR, PIN)
        
        if kelembapan is not None and suhu is not None:
            print("Suhu : {0:0.1f} C".format(suhu))
            print("Kelembapan : {0:0.1f} %".format(kelembapan))
        else:
            print("Gagal membaca data dari DHT11.")
        time.sleep(2.0)
except KeyboardInterrupt:
    print("Program dihentikan.")