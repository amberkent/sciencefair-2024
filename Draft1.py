import RPi.GPIO as GPIO
import time
#import Adafruit_ADS1x15
PWMpin=35
Pot_Pin=5
GAIN=1/327.67

#adc = Adafruit_ADS1x15.ADS1115()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Pot_Pin, GPIO.IN)
GPIO.setup(PWMpin,GPIO.OUT)
p = GPIO.PWM (PWMpin,100) #Frequenzy 50 = 50 hertz

while True:
    inputValue = GPIO.input(Pot_Pin)
    #value = adc.read_adc_difference(Pot_Pin, gain=GAIN)
    # the dutycycle for RPi.GPIO is 0-100:
    # See: https://raspberrypi.stackexchange.com/questions/114413/what-values-for-pwm-to-set-intensity-from-0-to-255#:~:text=0-,RPi.,and%2050%20is%20half%20power.
    dc=inputValue*GAIN
    print(f"Input: {inputValue} {dc}")
    p.ChangeDutyCycle(dc) 

# 0.05 = 0.05 seconds
time.sleep(0.05)
