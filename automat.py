import RPi.GPIO as GPIO
import time
import board
import busio
from adafruit_character_lcd.character_lcd_i2c import Character_LCD_I2C

# Configuration Variables
MOTOR_PINS = [17, 27, 22, 23, 24, 25]  # GPIO pins connected to relay IN1-IN6 for motors
BUTTON_PINS = [12, 13, 19, 16, 20, 21]  # GPIO pins connected to buttons
LIMIT_SWITCH_PINS = [26, 7, 8, 9, 10, 11]  # GPIO pins connected to limit switches
FAN_PIN = 5  # GPIO pin for fan
COOLING_PIN = 6  # GPIO pin for cooling
HEATING_PIN = 14  # GPIO pin for heating element
LIGHT_PIN = 15  # GPIO pin for light

# LCD Configuration
lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = Character_LCD_I2C(i2c, lcd_columns, lcd_rows)

# Timing and control variables
MOTOR_RUNTIME_LIMIT = 10  # Maximum time (in seconds) to run a motor if the limit switch fails
DRINK_COUNT = 6  # Number of drinks available

# Setup GPIO
GPIO.setmode(GPIO.BCM)

# Initialize motor pins
for motor_pin in MOTOR_PINS:
    GPIO.setup(motor_pin, GPIO.OUT)
    GPIO.output(motor_pin, GPIO.LOW)

# Initialize limit switch pins
for limit_switch_pin in LIMIT_SWITCH_PINS:
    GPIO.setup(limit_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize button pins
for button_pin in BUTTON_PINS:
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize other device pins
GPIO.setup(FAN_PIN, GPIO.OUT)
GPIO.setup(COOLING_PIN, GPIO.OUT)
GPIO.setup(HEATING_PIN, GPIO.OUT)
GPIO.setup(LIGHT_PIN, GPIO.OUT)

# Turn off all devices initially
GPIO.output(FAN_PIN, GPIO.LOW)
GPIO.output(COOLING_PIN, GPIO.LOW)
GPIO.output(HEATING_PIN, GPIO.LOW)
GPIO.output(LIGHT_PIN, GPIO.LOW)

# Function to update the LCD display
def update_lcd():
    lcd.clear()
    lcd.message = f"Drinks Left: {DRINK_COUNT}\nTemp: {get_temperature()}C"

# Function to simulate getting the current temperature (Replace with actual sensor reading)
def get_temperature():
    return round(20 + (time.time() % 10), 1)  # Example: returns a value between 20.0 and 29.9

# Function to run a motor until its limit switch is pressed or the time limit is reached
def run_motor_until_limit(motor_pin, limit_switch_pin):
    global DRINK_COUNT
    GPIO.output(motor_pin, GPIO.HIGH)  # Start the motor
    start_time = time.time()

    # Run motor until the limit switch is pressed or the time limit is reached
    while GPIO.input(limit_switch_pin) == GPIO.HIGH:
        if time.time() - start_time > MOTOR_RUNTIME_LIMIT:
            print(f"Motor on GPIO {motor_pin} timeout. Stopping motor.")
            break
        time.sleep(0.01)  # Short delay to prevent CPU overload

    GPIO.output(motor_pin, GPIO.LOW)  # Stop the motor
    print(f"Motor on GPIO {motor_pin} stopped.")
    DRINK_COUNT -= 1  # Decrease the drink count by one
    update_lcd()  # Update the LCD display with the new drink count

# Function to activate a device for a set duration
def activate_device(device_pin, duration):
    GPIO.output(device_pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(device_pin, GPIO.LOW)

# Function to control the fan
def control_fan(state):
    GPIO.output(FAN_PIN, GPIO.HIGH if state else GPIO.LOW)
    print("Fan turned", "on" if state else "off")

# Function to control the cooling system
def control_cooling(state):
    GPIO.output(COOLING_PIN, GPIO.HIGH if state else GPIO.LOW)
    print("Cooling system turned", "on" if state else "off")

# Function to control the heating element
def control_heating(state):
    GPIO.output(HEATING_PIN, GPIO.HIGH if state else GPIO.LOW)
    print("Heating element turned", "on" if state else "off")

# Function to control the light
def control_light(state):
    GPIO.output(LIGHT_PIN, GPIO.HIGH if state else GPIO.LOW)
    print("Light turned", "on" if state else "off")

# Main loop
try:
    update_lcd()  # Initialize LCD with initial values
    while True:
        for i, button_pin in enumerate(BUTTON_PINS):
            if GPIO.input(button_pin) == GPIO.LOW:  # Button pressed
                print(f"Button {i+1} pressed. Activating motor {i+1}.")
                run_motor_until_limit(MOTOR_PINS[i], LIMIT_SWITCH_PINS[i])
                time.sleep(0.5)  # Debounce delay
        
        # Example usage: control fan, cooling, heating, and light as needed
        # Uncomment these lines and replace 'True'/'False' with your conditions
        # control_fan(True)
        # control_cooling(True)
        # control_heating(True)
        # control_light(True)
        
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
