import RPi.GPIO as GPIO
import time
import pigpio
import Adafruit_DHT

peltier_pin = 17
dht_pin = 4
switch_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(peltier_pin, GPIO.OUT)
GPIO.setup(dht_pin, GPIO.IN)
GPIO.setup(switch_pin, GPIO.IN)

pi = pigpio.pi()

cooling_temperature = 25

heating_temperature = cooling_temperature - 5

max_current = 4.6

def read_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, dht_pin)

    if humidity is not None and temperature is not None:
        print("Temperature: {0:0.1f} C".format(temperature))
        return temperature
    else:
        print("Failed to read temperature")
        return None

def control_peltier(temperature):
    if temperature is not None:
        if temperature > cooling_temperature and temperature < heating_temperature:
            temperature_difference = temperature - cooling_temperature
            duty_cycle = temperature_difference / (25 - cooling_temperature)

            if duty_cycle > max_current:
                duty_cycle = max_current

            print("PWM duty cycle:", duty_cycle)
            pi.set_PWM_dutycycle(peltier_pin, duty_cycle)

        elif temperature >= heating_temperature:
            temperature_difference = heating_temperature - temperature
            duty_cycle = temperature_difference / (25 - heating_temperature)

            if duty_cycle > max_current:
                duty_cycle = max_current

            print("PWM duty cycle:", duty_cycle)
            pi.set_PWM_dutycycle(peltier_pin, duty_cycle)

        else:
            pi.set_PWM_dutycycle(peltier_pin, 0)
            print("Peltier cooler OFF")

while True:
    current_temperature = read_temperature()

    switch_state = GPIO.input(switch_pin)
    if switch_state:
        control_peltier(heating_temperature)
    else:
        control_peltier(cooling_temperature)

    time.sleep(10)
