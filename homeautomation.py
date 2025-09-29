Aim: IoT based Web Controlled Home Automation using Raspberry Pi
Connection scheme Raspberry Pi

TM1637 Board Pin RPi Pin
GND 6
VCC 2
IN1 26

Step 1: Type the following python program in Thonny.
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from time import sleep
relay_pin=26
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin,GPIO.OUT)
GPIO.output(relay_pin,1)
try:
while True:
GPIO.output(relay_pin,0)
sleep(5)
GPIO.output(relay_pin,1)
sleep(5)
except KeyboardInterrupt:
pass
GPIO.cleanup()