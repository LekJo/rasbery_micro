import board
import adafruit_dht
import time

# Gunakan GPIO04 (Pin Fisik 7)
dht = adafruit_dht.DHT11(board.D4)

print("Membaca Sensor DHT11 (Tekan Ctrl+C untuk berhenti)")
try:
    while True:
        try:
            suhu = dht.temperature
            kelembapan = dht.humidity
            
            if suhu is not None and kelembapan is not None:
                print(f"Suhu : {suhu:.1f} °C")
                print(f"Kelembapan : {kelembapan:.1f} %")
            else:
                print("Gagal membaca data.")
        except RuntimeError:
            time.sleep(2.0)
            continue
        time.sleep(2.0)
except KeyboardInterrupt:
    print("Program dihentikan.")
finally:
    dht.exit()