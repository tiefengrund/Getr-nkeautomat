# Raspberry Pi Drink and Snack Machine

This project controls a drink and snack vending machine using a Raspberry Pi. The machine dispenses drinks and snacks via motors, which are controlled by relays. It also features temperature control, lighting control, and a display to show the current temperature and the number of drinks left.

## Table of Contents
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Wiring Instructions](#wiring-instructions)
- [Software Setup](#software-setup)
- [Code Explanation](#code-explanation)
- [Images](#images)
  - [Wiring Diagram](#wiring-diagram)
  - [Final Setup](#final-setup)
- [License](#license)

## Features
- **Motor Control**: 6 motors for dispensing drinks and snacks, each controlled by a button and a limit switch.
- **Temperature Control**: A fan, cooling system, and heating element to maintain the desired temperature.
- **Lighting Control**: An adjustable lighting system controlled via a relay.
- **LCD Display**: Displays the number of drinks left and the current temperature.
- **Safety Features**: Includes a maximum runtime limit for motors to prevent overheating or damage.

## Hardware Requirements
- Raspberry Pi (any model with GPIO support)
- 2x 8-Relay Module
- 6x DC Motors (for dispensing drinks/snacks)
- 6x Limit Switches (for stopping the motors)
- 6x Push Buttons
- I2C LCD Display (16x2)
- Temperature Sensor (optional)
- Fan, Cooling System, Heating Element, and Light
- Wires, Resistors, Breadboard, Power Supply

## Wiring Instructions

### GPIO Pin Assignments

- **Motors** (connected to relay IN1-IN6):
  - Motor 1: GPIO 17
  - Motor 2: GPIO 27
  - Motor 3: GPIO 22
  - Motor 4: GPIO 23
  - Motor 5: GPIO 24
  - Motor 6: GPIO 25
- **Buttons**:
  - Button 1: GPIO 12
  - Button 2: GPIO 13
  - Button 3: GPIO 19
  - Button 4: GPIO 16
  - Button 5: GPIO 20
  - Button 6: GPIO 21
- **Limit Switches**:
  - Limit Switch 1: GPIO 26
  - Limit Switch 2: GPIO 7
  - Limit Switch 3: GPIO 8
  - Limit Switch 4: GPIO 9
  - Limit Switch 5: GPIO 10
  - Limit Switch 6: GPIO 11
- **Fan**: GPIO 5
- **Cooling**: GPIO 6
- **Heating**: GPIO 14
- **Light**: GPIO 15
- **I2C LCD**:
  - SDA: GPIO 2 (SDA)
  - SCL: GPIO 3 (SCL)

### Power and Ground
- Connect VCC (3.3V or 5V) to power the relay boards, LCD, and other components.
- Connect all GND pins from the Raspberry Pi, buttons, relay modules, and LCD to a common ground.

## Software Setup

### Step 1: Install Required Libraries

Ensure your Raspberry Pi has the necessary Python libraries installed.

```bash
sudo apt-get update
sudo apt-get install python3-pip
pip3 install RPi.GPIO adafruit-circuitpython-charlcd
