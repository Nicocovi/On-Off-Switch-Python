
#!/usr/bin/env python

# Import required Python libraries
import RPi.GPIO as GPIO
import time

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)

if(GPIO.input(11) ==1):
        GPIO.output(11,0)
        print("<h1>Lights off</h1>")
else:
        GPIO.output(11,1)
        print("<h1>Lights on</h1>")




