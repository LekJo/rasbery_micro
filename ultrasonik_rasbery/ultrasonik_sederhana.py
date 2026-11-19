import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def ukur_jarak():
    GPIO.output(TRIG, False)
    time.sleep(0.05) 
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        stop = time.time()

    durasi = stop - start
    jarak = durasi * 17150 # Rumus siap pakai
    return jarak

print("Membaca Sensor Ultrasonik (Tekan Ctrl+C untuk berhenti)")
try:
    while True:
        d = ukur_jarak()
        print("Jarak: {0:.2f} cm".format(d))
        time.sleep(1)
except KeyboardInterrupt:
    print("Program dihentikan.")
finally:
    GPIO.cleanup()