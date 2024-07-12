#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include "DHT.h"

#define DHTPIN 2     // DHT22 data pin
#define DHTTYPE DHT22
#define LDRPIN A0    // Photoresistor pin

// Relay pins
#define COOLING_PIN 3
#define HEATING_PIN 4
#define FAN_PIN 5
#define RELAY_PIN 6

// Button pins
const int BUTTON_PINS[6] = {7, 8, 9, 10, 11, 12};

// Number of drinks left for each button
int drinksLeft[6] = {5, 5, 5, 5, 5, 5};

// Initialize the DHT22 sensor
DHT dht(DHTPIN, DHTTYPE);

// Initialize the LCD
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  // Start serial communication
  Serial.begin(9600);

  // Initialize DHT22 sensor
  dht.begin();

  // Initialize LCD
  lcd.begin();
  lcd.backlight();

  // Initialize relay pins as output
  pinMode(COOLING_PIN, OUTPUT);
  pinMode(HEATING_PIN, OUTPUT);
  pinMode(FAN_PIN, OUTPUT);
  pinMode(RELAY_PIN, OUTPUT);

  // Initialize button pins as input
  for (int i = 0; i < 6; i++) {
    pinMode(BUTTON_PINS[i], INPUT_PULLUP);
  }

  // Initialize photoresistor pin as input
  pinMode(LDRPIN, INPUT);
}

void loop() {
  // Read temperature from DHT22
  float temperature = dht.readTemperature();

  // Read light level from photoresistor
  int lightLevel = analogRead(LDRPIN);

  // Control cooling, heating, and fan based on temperature
  if (!isnan(temperature)) {
    Serial.print("Temperature: ");
    Serial.println(temperature);

    if (temperature > 9) {
      digitalWrite(COOLING_PIN, HIGH);
      digitalWrite(HEATING_PIN, LOW);
      digitalWrite(FAN_PIN, HIGH);
    } else if (temperature < 7) {
      digitalWrite(COOLING_PIN, LOW);
      digitalWrite(HEATING_PIN, HIGH);
      digitalWrite(FAN_PIN, LOW);
    } else {
      digitalWrite(COOLING_PIN, LOW);
      digitalWrite(HEATING_PIN, LOW);
      digitalWrite(FAN_PIN, LOW);
    }
  } else {
    Serial.println("Failed to read temperature!");
  }

  // Control light based on light level
  if (lightLevel < 500) { // Adjust threshold as necessary
    lcd.backlight();
  } else {
    lcd.noBacklight();
  }

  // Handle button presses
  for (int i = 0; i < 6; i++) {
    if (digitalRead(BUTTON_PINS[i]) == LOW) {
      if (drinksLeft[i] > 0) {
        Serial.print("Button ");
        Serial.print(i + 1);
        Serial.println(" pressed");

        // Activate relay for motor
        digitalWrite(RELAY_PIN, HIGH);
        delay(1000);  // Relay on for 1 second
        digitalWrite(RELAY_PIN, LOW);

        // Decrement drink count
        drinksLeft[i]--;

        // Update LCD display
        updateDisplay(temperature);
      } else {
        Serial.print("No drinks left for button ");
        Serial.println(i + 1);
      }

      // Debounce delay
      delay(300);
    }
  }

  // Update display periodically
  updateDisplay(temperature);

  // Delay before next loop
  delay(1000);
}

void updateDisplay(float temperature) {
  lcd.clear();

  if (!isnan(temperature)) {
    lcd.setCursor(0, 0);
    lcd.print("Temp: ");
    lcd.print(temperature);
    lcd.print("C");
  } else {
    lcd.setCursor(0, 0);
    lcd.print("Temp: Error");
  }

  lcd.setCursor(0, 1);
  lcd.print("Drinks: ");
  for (int i = 0; i < 6; i++) {
    lcd.print(drinksLeft[i]);
  }
}
