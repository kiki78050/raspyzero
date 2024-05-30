from gpiozero import PWMLED
from time import sleep

# Erstellen Sie ein PWMLED-Objekt, das an Pin 17 angeschlossen ist
led = PWMLED(12)

try:
    while True:
        led.value = 0.2  # Setzt den Duty Cycle auf 20%
        sleep(5)         # Lässt die LED für eine Sekunde leuchten
        # Sie können sleep länger setzen, wenn Sie die LED kontinuierlich sehen möchten
except KeyboardInterrupt:
    led.close()  # Schaltet die LED sicher aus und gibt die Ressourcen frei
