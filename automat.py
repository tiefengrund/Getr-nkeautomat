import RPi.GPIO as GPIO
import time
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd
import adafruit_dht  # If using DHT22 sensor
import digitalio
from adafruit_bme280 import basic as adafruit_bme280  # For BME280 (alternative to DHT22)

# Pin Definitions
# Relay Module 1 (Snack Spirals)
SNACK_SPIRALS_PINS = [17, 27, 22, 23, 24, 25]  
# Relay Module 2 (Fan, Heating, Cooling)
FAN_PIN = 12
HEATING_PIN = 13
COOLING_PIN = 19
BUTTONS_PINS = [5, 6, 13, 19, 26, 21, 20, 16]  # All button pins
TEMP_SENSOR_PIN = 4  # GPIO pin for temperature sensor

# Setup GPIO
GPIO.setmode(GPIO.BCM)
for pin in SNACK_SPIRALS_PINS + [FAN_PIN, HEATING_PIN, COOLING_PIN]:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

for button_pin in BUTTONS_PINS:
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup I2C LCD
i2c = busio.I2C(board.SCL, board.SDA)
lcd_columns = 16
lcd_rows = 2
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows)
lcd.clear()

# Setup Temperature Sensor (DHT22)
dht_device = adafruit_dht.DHT22(board.D4)  # Use adafruit_bme280 for BME280 sensor

# Configuration dictionary
config = {
    'snack_spirals': {
        0: {'pin': 17, 'activation_time': 1},  # Motor 1
        1: {'pin': 27, 'activation_time': 1},  # Motor 2
        2: {'pin': 22, 'activation_time': 1},  # Motor 3
        3: {'pin': 23, 'activation_time': 1},  # Motor 4
        4: {'pin': 24, 'activation_time': 1},  # Motor 5
        5: {'pin': 25, 'activation_time': 1},  # Motor 6
    },
    'devices': {
        'fan': {'pin': FAN_PIN, 'activation_time': 2},
        'heating': {'pin': HEATING_PIN, 'activation_time': 2},
        'cooling': {'pin': COOLING_PIN, 'activation_time': 2},
    },
    'buttons': {
        0: {'device': 'snack_spirals', 'index': 0},
        1: {'device': 'snack_spirals', 'index': 1},
        2: {'device': 'snack_spirals', 'index': 2},
        3: {'device': 'snack_spirals', 'index': 3},
        4: {'device': 'snack_spirals', 'index': 4},
        5: {'device': 'snack_spirals', 'index': 5},
        6: {'device': 'devices', 'device_name': 'fan'},
        7: {'device': 'devices', 'device_name': 'heating'},
        8: {'device': 'devices', 'device_name': 'cooling'},
    }
}

# Function to activate relay
def activate_device(device_type, index=None, device_name=None):
    if device_type == 'snack_spirals':
        if index is not None:
            pin = config['snack_spirals'][index]['pin']
            activation_time = config['snack_spirals'][index]['activation_time']
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(activation_time)
            GPIO.output(pin, GPIO.LOW)
    elif device_type == 'devices':
        if device_name in config['devices']:
            pin = config['devices'][device_name]['pin']
            activation_time = config['devices'][device_name]['activation_time']
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(activation_time)
            GPIO.output(pin, GPIO.LOW)

# Function to get temperature from sensor
def get_temperature():
    try:
        # Using DHT22
        temperature_c = dht_device.temperature
        return temperature_c
    except RuntimeError as e:
        print(f"Error getting temperature: {e}")
        return None

# Function to update LCD display
def update_lcd(drinks_left, temperature):
    lcd.clear()
    lcd.message = f"Drinks Left: {drinks_left}\nTemp: {temperature:.1f}C"

# Main loop
try:
    drinks_left = 10  # Initial number of drinks (adjust as needed)
    update_interval = 60  # Update interval for temperature display (seconds)
    last_update_time = time.time()

    while True:
        # Check buttons
        for i, button_pin in enumerate(BUTTONS_PINS):
            if GPIO.input(button_pin) == GPIO.LOW:  # Button pressed
                button_config = config['buttons'].get(i)
                if button_config:
                    if button_config['device'] == 'snack_spirals':
                        activate_device('snack_spirals', index=button_config['index'])
                        drinks_left -= 1  # Decrement drinks count
                    elif button_config['device'] == 'devices':
                        activate_device('devices', device_name=button_config['device_name'])
                time.sleep(0.5)  # Debounce delay

        # Update LCD with temperature
        current_time = time.time()
        if current_time - last_update_time >= update_interval:
            temperature = get_temperature()
            if temperature is not None:
                update_lcd(drinks_left, temperature)
            last_update_time = current_time

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
