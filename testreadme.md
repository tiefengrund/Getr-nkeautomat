
markdown

# Raspberry Pi Getränke- und Snackmaschine

Dieses Projekt steuert eine Getränke- und Snackmaschine mit einem Raspberry Pi. Die Maschine gibt Getränke und Snacks über Motoren aus, die über Relais gesteuert werden. Sie verfügt auch über Temperaturregelung, Beleuchtungssteuerung und ein Display zur Anzeige der aktuellen Temperatur und der verbleibenden Anzahl an Getränken.

## Projektübersicht

### Hintergrund

Das Projekt zielt darauf ab, eine alte Getränkeausgabe aus dem Jahr 1989 in der Basis der freiwilligen Feuerwehr zu modernisieren. Der Plan ist, die Maschine mit einem Raspberry Pi neu zu gestalten, um sie zu einem lehrreichen Werkzeug für Kinder im Bereich Elektronik und Programmierung zu machen. Dieses Vorhaben bietet eine praktische Möglichkeit, sowohl die Technik hinter der Maschine zu verstehen als auch wichtige Fähigkeiten in der Programmierung und Hardware-Interfacing zu erlernen.

### Ziele
- **Modernisierung**: Die alte Maschine wird mit moderner Technik und Steuerungssystemen ausgestattet.
- **Bildung**: Kindern wird durch das Projekt Wissen in Elektronik und Programmierung vermittelt.
- **Erfahrung**: Praktisches Lernen durch Aufbau, Programmierung und Wartung des Systems.

## Inhaltsverzeichnis
- [Funktionen](#funktionen)
- [Hardware-Anforderungen](#hardware-anforderungen)
- [Verdrahtungsanweisungen](#verdrahtungsanweisungen)
- [Software-Einrichtung](#software-einrichtung)
- [Code-Erklärung](#code-erklärung)
- [Bilder](#bilder)
  - [Verdrahtungsdiagramm](#verdrahtungsdiagramm)
  - [Endsetup](#endsetup)
- [Lizenz](#lizenz)

## Funktionen
- **Motorsteuerung**: 6 Motoren für die Ausgabe von Getränken und Snacks, jeweils gesteuert durch einen Knopf und einen Endschalter.
- **Temperaturregelung**: Ein Ventilator, Kühlsystem und Heizelement zur Aufrechterhaltung der gewünschten Temperatur.
- **Beleuchtungssteuerung**: Ein anpassbares Beleuchtungssystem, das über ein Relais gesteuert wird.
- **LCD-Display**: Zeigt die verbleibende Anzahl an Getränken und die aktuelle Temperatur an.
- **Sicherheitsmerkmale**: Beinhaltet ein maximales Laufzeitlimit für Motoren, um Überhitzung oder Beschädigung zu verhindern.

## Hardware-Anforderungen
- Raspberry Pi (jedes Modell mit GPIO-Unterstützung)
- 2x 8-Relais-Modul
- 6x Gleichstrommotoren (für die Ausgabe von Getränken/Snacks)
- 6x Endschalter (zum Stoppen der Motoren)
- 6x Druckknöpfe
- I2C LCD-Display (16x2)
- Temperatursensor (optional)
- Ventilator, Kühlsystem, Heizelement und Licht
- Kabel, Widerstände, Steckbrett, Stromversorgung

## Verdrahtungsanweisungen

### GPIO-Pin-Zuweisungen

- **Motoren** (verbunden mit Relais IN1-IN6):
  - Motor 1: GPIO 17
  - Motor 2: GPIO 27
  - Motor 3: GPIO 22
  - Motor 4: GPIO 23
  - Motor 5: GPIO 24
  - Motor 6: GPIO 25
- **Knöpfe**:
  - Knopf 1: GPIO 12
  - Knopf 2: GPIO 13
  - Knopf 3: GPIO 19
  - Knopf 4: GPIO 16
  - Knopf 5: GPIO 20
  - Knopf 6: GPIO 21
- **Endschalter**:
  - Endschalter 1: GPIO 26
  - Endschalter 2: GPIO 7
  - Endschalter 3: GPIO 8
  - Endschalter 4: GPIO 9
  - Endschalter 5: GPIO 10
  - Endschalter 6: GPIO 11
- **Ventilator**: GPIO 5
- **Kühlung**: GPIO 6
- **Heizung**: GPIO 14
- **Licht**: GPIO 15
- **I2C LCD**:
  - SDA: GPIO 2 (SDA)
  - SCL: GPIO 3 (SCL)

### Stromversorgung und Erdung
- Verbinden Sie VCC (3,3V oder 5V), um die Relais-Boards, das LCD und andere Komponenten mit Strom zu versorgen.
- Verbinden Sie alle GND-Pins vom Raspberry Pi, Knöpfen, Relais-Modulen und LCD mit einer gemeinsamen Erdung.

## Software-Einrichtung

### Schritt 1: Benötigte Bibliotheken installieren

Stellen Sie sicher, dass Ihr Raspberry Pi die erforderlichen Python-Bibliotheken installiert hat.

```bash
sudo apt-get update
sudo apt-get install python3-pip
pip3 install RPi.GPIO adafruit-circuitpython-charlcd

Schritt 2: Repository klonen

Klonen Sie dieses Repository auf Ihren Raspberry Pi.

bash

git clone https://github.com/your-username/raspberry-pi-vending-machine.git
cd raspberry-pi-vending-machine

Schritt 3: Code ausführen

Um den Code auszuführen, geben Sie folgenden Befehl im Terminal ein:

bash

python3 vending_machine.py

Schritt 4: Verdrahtungsdiagramm

Beziehen Sie sich auf das folgende Diagramm, um die Komponenten korrekt zu verdrahten.
Code-Erklärung
Hauptmerkmale

    Motorsteuerung: Die Motoren werden über Relais gesteuert. Jeder Motor stoppt, wenn sein entsprechender Endschalter betätigt wird oder nach einer festgelegten Zeitüberschreitung.
    Temperaturregelung: Der Ventilator, die Kühlung und das Heizelement werden über GPIO-Pins gesteuert, die nach Bedarf ein- oder ausgeschaltet werden können.
    LCD-Display: Zeigt die verbleibende Anzahl an Getränken und die aktuelle Temperatur an, die nach jeder Aktion aktualisiert wird.
    Knopfsteuerung: Jeder Knopf entspricht einem bestimmten Motor und Endschalter und löst den Motor beim Drücken aus.

Funktionalität

    run_motor_until_limit(motor_pin, limit_switch_pin): Führt einen Motor aus, bis sein Endschalter betätigt wird oder das maximale Laufzeitlimit erreicht ist.
    activate_device(device_pin, duration): Aktiviert ein Gerät (z.B. Ventilator, Heizung) für eine bestimmte Dauer.
    update_lcd(): Aktualisiert das LCD mit der aktuellen Getränkezählung und Temperatur.

Bilder
Verdrahtungsdiagramm

Wird hinzugefügt.
Endsetup

Wird hinzugefügt.
Lizenz

Dieses Projekt ist lizenziert unter der GNU General Public License v3.0. Weitere Einzelheiten finden Sie in der LICENSE-Datei.

Certainly! Here's the complete README.md in markdown format for easy copy-pasting:

markdown

# Raspberry Pi Getränke- und Snackmaschine

Dieses Projekt steuert eine Getränke- und Snackmaschine mit einem Raspberry Pi. Die Maschine gibt Getränke und Snacks über Motoren aus, die über Relais gesteuert werden. Sie verfügt auch über Temperaturregelung, Beleuchtungssteuerung und ein Display zur Anzeige der aktuellen Temperatur und der verbleibenden Anzahl an Getränken.

## Projektübersicht

### Hintergrund

Das Projekt zielt darauf ab, eine alte Getränkeausgabe aus dem Jahr 1989 in der Basis der freiwilligen Feuerwehr zu modernisieren. Der Plan ist, die Maschine mit einem Raspberry Pi neu zu gestalten, um sie zu einem lehrreichen Werkzeug für Kinder im Bereich Elektronik und Programmierung zu machen. Dieses Vorhaben bietet eine praktische Möglichkeit, sowohl die Technik hinter der Maschine zu verstehen als auch wichtige Fähigkeiten in der Programmierung und Hardware-Interfacing zu erlernen.

### Ziele
- **Modernisierung**: Die alte Maschine wird mit moderner Technik und Steuerungssystemen ausgestattet.
- **Bildung**: Kindern wird durch das Projekt Wissen in Elektronik und Programmierung vermittelt.
- **Erfahrung**: Praktisches Lernen durch Aufbau, Programmierung und Wartung des Systems.

## Inhaltsverzeichnis
- [Funktionen](#funktionen)
- [Hardware-Anforderungen](#hardware-anforderungen)
- [Verdrahtungsanweisungen](#verdrahtungsanweisungen)
- [Software-Einrichtung](#software-einrichtung)
- [Code-Erklärung](#code-erklärung)
- [Bilder](#bilder)
  - [Verdrahtungsdiagramm](#verdrahtungsdiagramm)
  - [Endsetup](#endsetup)
- [Lizenz](#lizenz)

## Funktionen
- **Motorsteuerung**: 6 Motoren für die Ausgabe von Getränken und Snacks, jeweils gesteuert durch einen Knopf und einen Endschalter.
- **Temperaturregelung**: Ein Ventilator, Kühlsystem und Heizelement zur Aufrechterhaltung der gewünschten Temperatur.
- **Beleuchtungssteuerung**: Ein anpassbares Beleuchtungssystem, das über ein Relais gesteuert wird.
- **LCD-Display**: Zeigt die verbleibende Anzahl an Getränken und die aktuelle Temperatur an.
- **Sicherheitsmerkmale**: Beinhaltet ein maximales Laufzeitlimit für Motoren, um Überhitzung oder Beschädigung zu verhindern.

## Hardware-Anforderungen
- Raspberry Pi (jedes Modell mit GPIO-Unterstützung)
- 2x 8-Relais-Modul
- 6x Gleichstrommotoren (für die Ausgabe von Getränken/Snacks)
- 6x Endschalter (zum Stoppen der Motoren)
- 6x Druckknöpfe
- I2C LCD-Display (16x2)
- Temperatursensor (optional)
- Ventilator, Kühlsystem, Heizelement und Licht
- Kabel, Widerstände, Steckbrett, Stromversorgung

## Verdrahtungsanweisungen

### GPIO-Pin-Zuweisungen

- **Motoren** (verbunden mit Relais IN1-IN6):
  - Motor 1: GPIO 17
  - Motor 2: GPIO 27
  - Motor 3: GPIO 22
  - Motor 4: GPIO 23
  - Motor 5: GPIO 24
  - Motor 6: GPIO 25
- **Knöpfe**:
  - Knopf 1: GPIO 12
  - Knopf 2: GPIO 13
  - Knopf 3: GPIO 19
  - Knopf 4: GPIO 16
  - Knopf 5: GPIO 20
  - Knopf 6: GPIO 21
- **Endschalter**:
  - Endschalter 1: GPIO 26
  - Endschalter 2: GPIO 7
  - Endschalter 3: GPIO 8
  - Endschalter 4: GPIO 9
  - Endschalter 5: GPIO 10
  - Endschalter 6: GPIO 11
- **Ventilator**: GPIO 5
- **Kühlung**: GPIO 6
- **Heizung**: GPIO 14
- **Licht**: GPIO 15
- **I2C LCD**:
  - SDA: GPIO 2 (SDA)
  - SCL: GPIO 3 (SCL)

### Stromversorgung und Erdung
- Verbinden Sie VCC (3,3V oder 5V), um die Relais-Boards, das LCD und andere Komponenten mit Strom zu versorgen.
- Verbinden Sie alle GND-Pins vom Raspberry Pi, Knöpfen, Relais-Modulen und LCD mit einer gemeinsamen Erdung.

## Software-Einrichtung

### Schritt 1: Benötigte Bibliotheken installieren

Stellen Sie sicher, dass Ihr Raspberry Pi die erforderlichen Python-Bibliotheken installiert hat.

```bash
sudo apt-get update
sudo apt-get install python3-pip
pip3 install RPi.GPIO adafruit-circuitpython-charlcd

Schritt 2: Repository klonen

Klonen Sie dieses Repository auf Ihren Raspberry Pi.

bash

git clone https://github.com/your-username/raspberry-pi-vending-machine.git
cd raspberry-pi-vending-machine

Schritt 3: Code ausführen

Um den Code auszuführen, geben Sie folgenden Befehl im Terminal ein:

bash

python3 vending_machine.py

Schritt 4: Verdrahtungsdiagramm

Beziehen Sie sich auf das folgende Diagramm, um die Komponenten korrekt zu verdrahten.
Code-Erklärung
Hauptmerkmale

    Motorsteuerung: Die Motoren werden über Relais gesteuert. Jeder Motor stoppt, wenn sein entsprechender Endschalter betätigt wird oder nach einer festgelegten Zeitüberschreitung.
    Temperaturregelung: Der Ventilator, die Kühlung und das Heizelement werden über GPIO-Pins gesteuert, die nach Bedarf ein- oder ausgeschaltet werden können.
    LCD-Display: Zeigt die verbleibende Anzahl an Getränken und die aktuelle Temperatur an, die nach jeder Aktion aktualisiert wird.
    Knopfsteuerung: Jeder Knopf entspricht einem bestimmten Motor und Endschalter und löst den Motor beim Drücken aus.

Funktionalität

    run_motor_until_limit(motor_pin, limit_switch_pin): Führt einen Motor aus, bis sein Endschalter betätigt wird oder das maximale Laufzeitlimit erreicht ist.
    activate_device(device_pin, duration): Aktiviert ein Gerät (z.B. Ventilator, Heizung) für eine bestimmte Dauer.
    update_lcd(): Aktualisiert das LCD mit der aktuellen Getränkezählung und Temperatur.

Bilder
Verdrahtungsdiagramm

Wird hinzugefügt.
Endsetup

Wird hinzugefügt.
Lizenz

Dieses Projekt ist lizenziert unter der GNU General Public License v3.0. Weitere Einzelheiten finden Sie in der LICENSE-Datei.
Raspberry Pi Drink and Snack Machine

This project controls a drink and snack vending machine using a Raspberry Pi. The machine dispenses drinks and snacks via motors, which are controlled by relays. It also features temperature control, lighting control, and a display to show the current temperature and the number of drinks left.
Project Overview
Background

The project aims to modernize an old drink machine from 1989 at the volunteer firefighters' base. The plan is to rebuild the machine using a Raspberry Pi to create an educational tool for kids in electronics and programming. This project provides a hands-on way to understand both the technology behind the machine and to gain valuable skills in programming and hardware interfacing.
Goals

    Modernization: Updating the old machine with modern technology and control systems.
    Education: Teaching kids about electronics and programming through the project.
    Experience: Providing practical learning through the assembly, programming, and maintenance of the system.

Table of Contents

    Features
    Hardware Requirements
    Wiring Instructions
    Software Setup
    Code Explanation
    Images
        Wiring Diagram
        Final Setup
    License

Features

    Motor Control: 6 motors for dispensing drinks and snacks, each controlled by a button and a limit switch.
    Temperature Control: A fan, cooling system, and heating element to maintain the desired temperature.
    Lighting Control: An adjustable lighting system controlled via a relay.
    LCD Display: Displays the number of drinks left and the current temperature.
    Safety Features: Includes a maximum runtime limit for motors to prevent overheating or damage.

Hardware Requirements

    Raspberry Pi (any model with GPIO support)
    2x 8-Relay Module
    6x DC Motors (for dispensing drinks/snacks)
    6x Limit Switches (for stopping the motors)
    6x Push Buttons
    I2C LCD Display (16x2)
    Temperature Sensor (optional)
    Fan, Cooling System, Heating Element, and Light
    Wires, Resistors, Breadboard, Power Supply

Wiring Instructions
GPIO Pin Assignments

    Motors (connected to Relay IN1-IN6):
        Motor 1: GPIO 17
        Motor 2: GPIO 27
        Motor 3: GPIO 22
        Motor 4: GPIO 23
        Motor 5: GPIO 24
        Motor 6: GPIO 25
    Buttons:
        Button 1: GPIO 12
        Button 2: GPIO 13
        Button 3: GPIO 19
        Button 4: GPIO 16
        Button 5: GPIO 20
        Button 6: GPIO 21
    Limit Switches:
        Limit Switch 1: GPIO 26
        Limit Switch 2: GPIO 7
        Limit Switch 3: GPIO 8
        Limit Switch 4: GPIO 9
        Limit Switch 5: GPIO 10
        Limit Switch 6: GPIO 11
    Fan: GPIO 5
    Cooling: GPIO 6
    Heating: GPIO 14
    Light: GPIO 15
    I2C LCD:
        SDA: GPIO 2 (SDA)
        SCL: GPIO 3 (SCL)

Power and Grounding

    Connect VCC (3.3V or 5V) to power the relay boards, LCD, and other components.
    Connect all GND pins from the Raspberry Pi, buttons, relay modules, and LCD to a common ground.

Software Setup
Step 1: Install Required Libraries

Ensure your Raspberry Pi has the necessary Python libraries installed.

bash

sudo apt-get update
sudo apt-get install python3-pip
pip3 install RPi.GPIO adafruit-circuitpython-charlcd

Step 2: Clone Repository

Clone this repository onto your Raspberry Pi.

bash

git clone https://github.com/your-username/raspberry-pi-vending-machine.git
cd raspberry-pi-vending-machine

Step 3: Run Code

To execute the code, run the following command in the terminal:

bash

python3 vending_machine.py

Step 4: Wiring Diagram

Refer to the following diagram for correct component wiring.
Code Explanation
Main Features

    Motor Control: Motors are controlled via relays. Each motor stops when its respective limit switch is triggered or after a set timeout.
    Temperature Control: Fan, cooling, and heating elements are controlled via GPIO pins, which can be turned on or off as needed.
    LCD Display: Shows the remaining number of drinks and current temperature, updated after each action.
    Button Control: Each button corresponds to a specific motor and limit switch, triggering the motor when pressed.

Functionality

    run_motor_until_limit(motor_pin, limit_switch_pin): Runs a motor until its limit switch is triggered or the maximum runtime limit is reached.
    activate_device(device_pin, duration): Activates a device (e.g., fan, heater) for a specified duration.
    update_lcd(): Updates the LCD with the current drink count and temperature.

Images
Wiring Diagram

To be added.
Final Setup

To be added.
License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.