from gpiozero import LED
from time import sleep

led = LED(17)   # use gpio17 port

while True:  # repeat forever
    led.on()  # light on
    sleep(1)  # light off
    led.off()
    sleep(1)