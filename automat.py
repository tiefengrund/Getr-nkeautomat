import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import spidev
from lcd import drivers

# Pin Definitions
TEMP_SENSOR_PIN = 4  # GPIO pin for DHT22 sensor
LDR_CHANNEL = 0      # MCP3008 channel for LDR
COOLER_PIN = 17      # GPIO pin for cooler
HEATER_PIN = 27      # GPIO pin for heater
LIGHT_PIN = 22       # GPIO pin for light
RELAY_PIN = 23       # GPIO pin for relay
BUTTON_PINS = [5, 6, 13, 19, 26, 21]  # GPIO pins for buttons

# Constants
TEMP_MIN = 7         # Minimum temperature in Celsius
TEMP_MAX = 9         # Maximum temperature in Celsius
LIGHT_THRESHOLD = 500  # LDR threshold for light
DHT_SENSOR = Adafruit_DHT.DHT22

# Initialize MCP3008 SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

# Initialize LCD
display = drivers.Lcd()

# Drink counts
drinks_left = [5, 5, 5, 5, 5, 5]

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(COOLER_PIN, GPIO.OUT)
GPIO.setup(HEATER_PIN, GPIO.OUT)
GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.setup(RELAY_PIN, GPIO.OUT)

for pin in BUTTON_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to read from MCP3008
def read_adc(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# Function to control temperature
def control_temperature(temp):
    if temp > TEMP_MAX:
        GPIO.output(COOLER_PIN, GPIO.HIGH)
        GPIO.output(HEATER_PIN, GPIO.LOW)
    elif temp < TEMP_MIN:
        GPIO.output(COOLER_PIN, GPIO.LOW)
        GPIO.output(HEATER_PIN, GPIO.HIGH)
    else:
        GPIO.output(COOLER_PIN, GPIO.LOW)
        GPIO.output(HEATER_PIN, GPIO.LOW)

# Function to control light
def control_light(ldr_value):
    if ldr_value < LIGHT_THRESHOLD:
        GPIO.output(LIGHT_PIN, GPIO.HIGH)
    else:
        GPIO.output(LIGHT_PIN, GPIO.LOW)

# Function to select drink
def select_drink(drink_number):
    if drinks_left[drink_number - 1] > 0:
        drinks_left[drink_number - 1] -= 1
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        time.sleep(1)  # Simulate dispensing time
        GPIO.output(RELAY_PIN, GPIO.LOW)
        display.lcd_display_string(f"Drink {drink_number} selected", 1)
        display.lcd_display_string(f"Remaining: {drinks_left[drink_number - 1]}", 2)
        time.sleep(2)
    else:
        display.lcd_display_string(f"Drink {drink_number} sold out", 1)
        time.sleep(2)
    display.lcd_clear()

try:
    while True:
        # Read temperature
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, TEMP_SENSOR_PIN)
        
        # Read LDR value
        ldr_value = read_adc(LDR_CHANNEL)
        
        # Control temperature and light
        control_temperature(temperature)
        control_light(ldr_value)
        
        # Display temperature and light status on LCD
        display.lcd_display_string(f"Temp: {temperature:.1f}C", 1)
        display.lcd_display_string(f"Light: {ldr_value}", 2)
        
        # Check for button presses
        for i, button_pin in enumerate(BUTTON_PINS):
            if GPIO.input(button_pin) == GPIO.LOW:
                select_drink(i + 1)
                time.sleep(0.5)  # Debounce

        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    display.lcd_clear()
    GPIO.cleanup()
    spi.close()
