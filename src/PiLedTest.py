import RPi.GPIO as GPIO  # Import RPi.GPIO module
from time import sleep
from src import hal_input_switch  # Import the custom module for switch reading

# Initialize the GPIO for the switch
hal_input_switch.init()

# Set up GPIO pin for LED
LED_PIN = 24  # GPIO 24 for LED
GPIO.setmode(GPIO.BCM) 
GPIO.setup(LED_PIN, GPIO.OUT)  

try:
    while True:
        # Check the position of the slide switch
        if hal_input_switch.read_slide_switch() == 1:
            # Switch is in the left position, blink the LED at 5Hz (0.1s interval)
            GPIO.output(LED_PIN, GPIO.HIGH)
            sleep(0.1)
            GPIO.output(LED_PIN, GPIO.LOW)
            sleep(0.1)
        else:
            # Switch is in the right position, turn the LED off
            GPIO.output(LED_PIN, GPIO.LOW)

except KeyboardInterrupt:
    # Clean up GPIO settings when interrupted
    GPIO.cleanup()
