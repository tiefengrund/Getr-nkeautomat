import time
import Adafruit_DHT
from gpiozero import LED, Button, DigitalOutputDevice
from datetime import datetime
import threading
from Adafruit_CharLCD import Adafruit_CharLCD

# Setup GPIO pins
TEMP_SENSOR_PIN = 4  # temperature sensor
COOLING_PIN = 17  # cooling system
HEATING_PIN = 27  # heating system
FAN_PIN = 22  # fan
LIGHT_PIN = 5  # light
RELAY_PIN = 13  # relay

# GPIO pins for the buttons
BUTTON_PINS = [6, 12, 16, 20, 21, 26]  # 6 Fächer

# Initialize GPIO devices
cooling = DigitalOutputDevice(COOLING_PIN)
heating = DigitalOutputDevice(HEATING_PIN)
fan = DigitalOutputDevice(FAN_PIN)
light = LED(LIGHT_PIN)
buttons = [Button(pin) for pin in BUTTON_PINS]
relay = DigitalOutputDevice(RELAY_PIN)

# DHT sensor setup
DHT_SENSOR = Adafruit_DHT.DHT22

# Setup LCD display
lcd_columns = 16
lcd_rows = 2
lcd = Adafruit_CharLCD()

# Hier müssen wir zählen wieviel ins Fach passt
drinks_left = [5, 5, 5, 5, 5, 5]

def update_display():
    temperature = get_temperature()
    if temperature is not None:
        temp_str = f"Temp: {temperature:.1f}C"
    else:
        temp_str = "Temp: Error"

    drinks_str = "Drinks: " + "".join([str(d) for d in drinks_left])
    
    lcd.clear()
    lcd.message(temp_str + "\n" + drinks_str)

def get_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, TEMP_SENSOR_PIN)
    return temperature

def control_temperature():
    while True:
        temperature = get_temperature()
        if temperature is not None:
            print(f"Current Temperature: {temperature:.2f}°C")
            if temperature > 9:
                cooling.on()
                heating.off()
                fan.on()
            elif temperature < 7:
                cooling.off()
                heating.on()
                fan.off()
            else:
                cooling.off()
                heating.off()
                fan.off()
        else:
            print("Failed to retrieve temperature data.")
        update_display()
        time.sleep(10)

def control_light():
    while True:
        current_time = datetime.now().time()
        if current_time.hour >= 20 or current_time.hour < 6:  # Wir können hier auch noch einen fotosensor einbauen
            light.on()
        else:
            light.off()
        time.sleep(60)

def control_relay(button_index):
    print(f"Button {button_index + 1} pressed, activating relay for the motor...")
    relay.on()
    time.sleep(1)  # hier müssen wir testen wie lange der drehen muss
    relay.off()
    print("Relay deactivated.")

def handle_button_press():
    while True:
        for i, button in enumerate(buttons):
            if button.is_pressed:
                if drinks_left[i] > 0:
                    control_relay(i)
                    drinks_left[i] -= 1
                    update_display()
                else:
                    print(f"No drinks left for button {i + 1}.")
                while button.is_pressed:  # Wait until button is released
                    time.sleep(0.1)


// Hans und Ille trinken Bier
// Ille: Zum Wohl ihr Fotzen
// Ille: shut the fuck up fuckin cunts
if __name__ == = threading.Thread(target=control_temperature)
    light_threa"__main__":
    temp_thread d = threading.Thread(target=control_light)
    button_thread = threading.Thread(target=handle_button_press)

    temp_thread.start()
    light_thread.start()
    button_thread.start()

    temp_thread.join()
    light_thread.join()
    button_thread.join()
