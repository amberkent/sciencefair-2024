import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PWMpin=0
GPIO.setup(PWMpin,GPIO.OUT)

p = GPIO.PWM (PWMpin,50) #Frequenzy 50 = 50 hertz

            
