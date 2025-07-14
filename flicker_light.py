from gpiozero import LED, Button
from time import sleep

led_red = LED(13)   # use gpio 19 port
led_green = LED(19)
button_red = Button(21)
button_green = Button(16)

while True:
    if button_green.is_pressed:
        led_green.on()
        sleep(0.3)
        if button_green.is_pressed:
            led_green.off()
            sleep(0.3)
        elif button_red.is_pressed:
            led_red.on()
            sleep(0.3)
    elif button_red.is_pressed:
        led_red.on()
        sleep(0.3)
        if button_red.is_pressed:
            led_red.off()
            sleep(0.3)
        elif button_green.is_pressed:
            led_green.on()
            sleep(0.3)
