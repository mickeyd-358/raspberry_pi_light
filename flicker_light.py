from gpiozero import LED, Button
from time import sleep

led = LED(19)   # use gpio 19 port
button = Button(16)

while True:  # repeat forever
    button.wait_for_press()
    led.on()
    sleep(0.2)
    button.wait_for_press()
    led.off()
    sleep(0.2)