import RPi.GPIO as GPIO
import time
import adafruit_ads1x15.ads1115 as ADS
import adafruit_tsl2591
import board
import busio
from adafruit_ads1x15.analog_in import AnalogIn

PWMpin=19
GAIN=100/24300

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMpin,GPIO.OUT)
p = GPIO.PWM(PWMpin,0.25) #Frequenzy 50 = 50 hertz
p.start(0)

i2c = board.I2C()
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan_potentiometer = AnalogIn(ads, ADS.P0)

while True:
    value = chan_potentiometer.value
    # the dutycycle for RPi.GPIO is 0-100:
    # See: https://raspberrypi.stackexchange.com/questions/114413/what-values-for-pwm-to-set-intensity-from-0-to-255#:~:text=0-,RPi.,and%2050%20is%20half%20power.
    dc= min(max(value*GAIN, 0), 100)
    print(f"Input: {value} {dc}")
    p.ChangeDutyCycle(dc)

# 0.05 = 0.05 seconds
time.sleep(0.05)
