# this program blinks the led
import RPi.GPIO as GPIO
import time
pin=7;
delay=1;
GPIO.setmode(GPIO.BOARD); # Pin numbers as in physical board
GPIO.setup(pin, GPIO.OUT) # Define Pin as output
def blinkLED():
    GPIO.output (pin, GPIO.HIGH)
    time.sleep(delay);
    GPIO.output (pin, GPIO.LOW)
    time.sleep(delay);

for i in range(0,5):
    blinkLED();
GPIO.cleanup() # Set GPIO to initial conditions