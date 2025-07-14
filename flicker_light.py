from gpiozero import LED, Button
from time import sleep

led_red = LED(13)   # use gpio 19 port
led_green = LED(19)
button_red = Button(21)
button_green = Button(16)

while True:  # repeat forever
    button_red.wait_for_press()
    led_red.on()
    sleep(0.6)
    button_red.wait_for_press()
    led_red.off()
    sleep(0.6)
    button_green.wait_for_press()
    led_green.on()
    sleep(0.6)
    button_green.wait_for_press()
    led_green.off()
    sleep(0.6)