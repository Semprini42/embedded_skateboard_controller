import machine
from machine import Pin
import time
from BLE import ESP32_BLE

# defines a BLE object 
ble = ESP32_BLE("ESP32")

# Define the input pin for the PWM signal from the hoverboard radio controller
pwm_pin = Pin(23, Pin.OUT)

# Set up a PWM object on the input pin
pwm = machine.PWM(pwm_pin, freq = 1000)
pwm.duty(0)

# set pwm pulses for 5 seconds

while True:
    val = int(ble.message) if (ble.message.isdigit()) else -1
    # ble.message = ''0
    if (val >= 0 and val <= 1023):
        pwm.duty(val)