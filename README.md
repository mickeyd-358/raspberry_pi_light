# Two Lights & Two Buttons Raspberry Pi Project
This is my first project using the Raspberry Pi. In this project, I am controlling two separate LEDs (red and green) with two individual coloured push buttons. The code uses the gpiozero library to manage the inputs and outputs.

#  Features
Controls a Red LED and a Green LED.

Uses two push buttons to interact with the lights.

Implemented using the user-friendly gpiozero library.

Demonstrates simultaneous control and interaction with multiple GPIO components.

# Hardware Requirements

- Raspberry Pi (any model with GPIO pins, e.g., Pi 3, Pi 4, Pi Zero W)

- 2 x LEDs (e.g., one Red, one Green)

- 2 x Resistors (220 Ohm or 330 Ohm recommended for standard LEDs)

- 2 x Push Buttons (momentary switches)

- Multiple Jumper Wires (male-to-male)

- Breadboard (highly recommended for easy prototyping)

#  Wiring

### Red LED Circuit:

Connect one end of a jumper wire to GPIO Pin 13 (BCM numbering) on your Raspberry Pi.

Connect the other end of that jumper wire to one leg of a 220/330 Ohm Resistor on your breadboard.

Connect the other leg of the resistor to the LONG LEG (Anode) of your Red LED.

Connect the SHORT LEG (Cathode) of your Red LED to a jumper wire, and connect that to any GND (Ground) pin on your Raspberry Pi.

### Green LED Circuit:

Connect one end of a jumper wire to GPIO Pin 19 (BCM numbering) on your Raspberry Pi.

Connect the other end of that jumper wire to one leg of a 220/330 Ohm Resistor on your breadboard.

Connect the other leg of the resistor to the LONG LEG (Anode) of your Green LED.

Connect the SHORT LEG (Cathode) of your Green LED to a jumper wire, and connect that to any GND (Ground) pin on your Raspberry Pi.

### Red Button Connection:

Connect one leg of your Red Push Button to GPIO Pin 21 (BCM numbering) on your Raspberry Pi.

Connect the other leg of the Red Push Button to any GND (Ground) pin on your Raspberry Pi.

### Green Button Connection:

Connect one leg of your Green Push Button to GPIO Pin 16 (BCM numbering) on your Raspberry Pi.

Connect the other leg of the Green Push Button to any GND (Ground) pin on your Raspberry Pi.

# Software Requirements (on Raspberry Pi)
This project assumes you have a Raspberry Pi set up with Raspberry Pi OS and SSH enabled.

When the Green button is pressed, the Green LED turns on for 0.3 seconds. If the Green button is still pressed after that, the Green LED turns off for 0.3 seconds. Otherwise, if the Red button is pressed, the Red LED turns on for 0.3 seconds.

A similar logic applies when the Red button is pressed.

To stop the script: Press Ctrl+C in terminal.