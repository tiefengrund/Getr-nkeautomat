import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import spidev

# LCD Configuration
LCD_COLUMNS = 16
LCD_ROWS = 2
lcd_rs = digitalio.DigitalInOut(board.D4)
lcd_en = digitalio.DigitalInOut(board.D5)
lcd_d4 = digitalio.DigitalInOut(board.D6)
lcd_d5 = digitalio.DigitalInOut(board.D13)
lcd_d6 = digitalio.DigitalInOut(board.D19)
lcd_d7 = digitalio.DigitalInOut(board.D26)
lcd_backlight = digitalio.DigitalInOut(board.D21)

lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, LCD_COLUMNS, LCD_ROWS, lcd_backlight
)

# DHT22 Sensor Configuration
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # GPIO pin where the sensor is connected

# GPIO Pins for Motors, Buttons, and Devices
MOTORS = [17, 27, 22, 23, 24, 25]
BUTTONS = [12, 13, 19, 16, 20, 21]
LIMIT_SWITCHES = [26, 7, 8, 9, 10, 11]
FAN_PIN = 5
COOLING_PIN = 6
HEATING_PIN = 14
LIGHT_PIN = 15

# Photoresistor (LDR) Configuration
LDR_CHANNEL = 0  # Analog input channel for LDR
SPIDEV = spidev.SpiDev()
SPIDEV.open(0, 0)  # SPI bus 0, device (CS) 0
SPIDEV.max_speed_hz = 1350000

# Configuration for the number of drinks
DRINKS_LEFT = [10, 10, 10, 10, 10, 10]  # Initial count of drinks for each button

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Setup Motors
for motor in MOTORS:
    GPIO.setup(motor, GPIO.OUT)
    GPIO.output(motor, GPIO.LOW)

# Setup Buttons
for button in BUTTONS:
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup Limit Switches
for switch in LIMIT_SWITCHES:
    GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup Fan, Cooling, Heating, and Light
GPIO.setup(FAN_PIN, GPIO.OUT)
GPIO.setup(COOLING_PIN, GPIO.OUT)
GPIO.setup(HEATING_PIN, GPIO.OUT)
GPIO.setup(LIGHT_PIN, GPIO.OUT)

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        return None, None

def read_ldr():
    """Read the value from the LDR using SPI."""
    adc = SPIDEV.xfer2([1, (8 + LDR_CHANNEL) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def update_lcd(temperature, humidity, drinks_left):
    lcd.clear()
    lcd.message = f"Temp: {temperature:.1f}C\nHum: {humidity:.1f}%\nDrinks: {drinks_left}"

def run_motor_until_limit(motor_pin, limit_switch_pin):
    GPIO.output(motor_pin, GPIO.HIGH)
    while GPIO.input(limit_switch_pin) == GPIO.HIGH:
        time.sleep(0.1)
    GPIO.output(motor_pin, GPIO.LOW)

def activate_device(device_pin, duration):
    GPIO.output(device_pin, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(device_pin, GPIO.LOW)

def control_cooling_heating(temperature):
    cooling_active = False
    heating_active = False
    
    if temperature > 7:
        GPIO.output(COOLING_PIN, GPIO.HIGH)
        cooling_active = True
    else:
        GPIO.output(COOLING_PIN, GPIO.LOW)
    
    if temperature < 3:
        GPIO.output(HEATING_PIN, GPIO.HIGH)
        heating_active = True
    else:
        GPIO.output(HEATING_PIN, GPIO.LOW)
    
    # Control the fan based on cooling or heating status
    if cooling_active or heating_active:
        GPIO.output(FAN_PIN, GPIO.HIGH)
    else:
        GPIO.output(FAN_PIN, GPIO.LOW)

def control_light():
    ldr_value = read_ldr()
    if ldr_value < 500:  # Adjust threshold as needed
        GPIO.output(LIGHT_PIN, GPIO.HIGH)
    else:
        GPIO.output(LIGHT_PIN, GPIO.LOW)

def main():
    global DRINKS_LEFT
    
    while True:
        temperature, humidity = read_sensor()
        if temperature is not None and humidity is not None:
            for index, button_pin in enumerate(BUTTONS):
                if GPIO.input(button_pin) == GPIO.LOW:
                    if DRINKS_LEFT[index] > 0:
                        print(f"Button {index + 1} pressed")
                        motor_pin = MOTORS[index]
                        limit_switch_pin = LIMIT_SWITCHES[index]
                        run_motor_until_limit(motor_pin, limit_switch_pin)
                        DRINKS_LEFT[index] -= 1  # Decrease the drink count
                        update_lcd(temperature, humidity, DRINKS_LEFT[index])
                    else:
                        lcd.clear()
                        lcd.message = "Out of stock!"
                    # Delay to prevent multiple triggers
                    time.sleep(1)
            
            # Control Cooling, Heating, and Light
            control_cooling_heating(temperature)
            control_light()
        
        # Example usage: Activate fan for 5 seconds
        activate_device(FAN_PIN, 5)
        
        # Update every 10 seconds
        time.sleep(10)

if __name__ == "__main__":
    main()
