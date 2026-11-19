import RPi.GPIO as GPIO
import time

TRIG = 23 # Pin Fisik 16
ECHO = 24 # Pin Fisik 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def ukur_jarak():
    GPIO.output(TRIG, False)
    time.sleep(0.05) 
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    timeout = time.monotonic() + 0.05
    while GPIO.input(ECHO) == 0:
        if time.monotonic() > timeout: return None
    start = time.monotonic()

    timeout = start + 0.05
    while GPIO.input(ECHO) == 1:
        if time.monotonic() > timeout: return None
    stop = time.monotonic()

    durasi = stop - start
    jarak = durasi * 34300 / 2
    return jarak

print("Membaca Sensor Ultrasonik (Tekan Ctrl+C untuk berhenti)")
try:
    while True:
        d = ukur_jarak()
        if d is not None:
            print(f"Jarak: {d:.2f} cm")
        else:
            print("Gagal membaca jarak (Timeout).")
        time.sleep(1)
except KeyboardInterrupt:
    print("Program dihentikan.")
finally:
    GPIO.cleanup()