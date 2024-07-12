# Raspberry Pi Drinks Machine Wiring Documentation

## Components
- **Raspberry Pi**
- **16x2 I2C LCD Display**
- **DHT22 Temperature Sensor**
- **Photoresistor (LDR)**
- **MCP3008 ADC**
- **6 Push Buttons**
- **4 Relays for controlling cooling, heating, fan, and motor**
- **LED for light control**
- **10kΩ resistors**
- **220Ω resistor for LED**
- **Breadboard and connecting wires**

## GPIO Pin Assignments
- **DHT22**: GPIO4
- **Photoresistor (LDR)**: Analog input via MCP3008 (CH0)
- **Buttons**: GPIO6, GPIO12, GPIO16, GPIO20, GPIO21, GPIO26
- **Relays**: GPIO17 (Cooling), GPIO27 (Heating), GPIO22 (Fan), GPIO13 (Motor)
- **LED**: GPIO5
- **I2C LCD**: SDA (GPIO2), SCL (GPIO3)

## Wiring Diagram

### 1. DHT22 Temperature Sensor
- **VCC**: Connect to 3.3V
- **GND**: Connect to GND
- **Data**: Connect to GPIO4 (use a pull-up resistor of 10kΩ between Data and 3.3V if necessary)

### 2. Photoresistor (LDR) and MCP3008
- **MCP3008**:
  - **VDD**: Connect to 3.3V
  - **VREF**: Connect to 3.3V
  - **AGND**: Connect to GND
  - **DGND**: Connect to GND
  - **CLK**: Connect to GPIO11
  - **DOUT**: Connect to GPIO9
  - **DIN**: Connect to GPIO10
  - **CS/SHDN**: Connect to GPIO8

- **Photoresistor (LDR)**:
  - One leg of LDR to 3.3V
  - Other leg of LDR to MCP3008 CH0 (Analog input) and to GND via a 10kΩ resistor

### 3. Push Buttons
- One leg of each button to GND
- Other leg of each button to GPIO pins:
  - Button 1: GPIO6
  - Button 2: GPIO12
  - Button 3: GPIO16
  - Button 4: GPIO20
  - Button 5: GPIO21
  - Button 6: GPIO26
- (Optional) Use 10kΩ pull-down resistors between GPIO pins and GND if necessary

### 4. Relays
- **Cooling (Relay 1)**: GPIO17
- **Heating (Relay 2)**: GPIO27
- **Fan (Relay 3)**: GPIO22
- **Motor (Relay 4)**: GPIO13
- Each relay module's VCC to 5V, GND to GND, and IN pin to respective GPIO pin

### 5. LED
- Anode (+) to GPIO5 via a 220Ω current-limiting resistor
- Cathode (-) to GND

### 6. I2C LCD Display
- **SDA**: Connect to GPIO2 (SDA)
- **SCL**: Connect to GPIO3 (SCL)
- **VCC**: Connect to 5V
- **GND**: Connect to GND

## Complete Wiring Table

| Component            | Pin             | Raspberry Pi GPIO Pin  | Note                                      |
|----------------------|-----------------|------------------------|-------------------------------------------|
| **DHT22**            | VCC             | 3.3V                   |                                           |
|                      | GND             | GND                    |                                           |
|                      | Data            | GPIO4                  |                                           |
| **Photoresistor**    | Leg 1           | 3.3V                   |                                           |
|                      | Leg 2           | MCP3008 CH0 & GND (via 10kΩ) |                                      |
| **MCP3008**          | VDD             | 3.3V                   |                                           |
|                      | VREF            | 3.3V                   |                                           |
|                      | AGND            | GND                    |                                           |
|                      | DGND            | GND                    |                                           |
|                      | CLK             | GPIO11                 |                                           |
|                      | DOUT            | GPIO9                  |                                           |
|                      | DIN             | GPIO10                 |                                           |
|                      | CS/SHDN         | GPIO8                  |                                           |
| **Button 1**         | Leg 1           | GND                    |                                           |
|                      | Leg 2           | GPIO6                  |                                           |
| **Button 2**         | Leg 1           | GND                    |                                           |
|                      | Leg 2           | GPIO12                 |                                           |
| **Button 3**         | Leg 1           | GND                    |                                           |
|                      | Leg 2           | GPIO16                 |                                           |
| **Button 4**         | Leg 1           | GND                    |                                           |
|                      | Leg 2           | GPIO20                 |                                           |
| **Button 5**         | Leg 1           | GND                    |                                           |
|                      | Leg 2           | GPIO21                 |                                           |
| **Button 6**         | Leg 1           | GND                    |                                           |
|                      | Leg 2           | GPIO26                 |                                           |
| **Cooling Relay**    | VCC             | 5V                     |                                           |
|                      | GND             | GND                    |                                           |
|                      | IN              | GPIO17                 |                                           |
| **Heating Relay**    | VCC             | 5V                     |                                           |
|                      | GND             | GND                    |                                           |
|                      | IN              | GPIO27                 |                                           |
| **Fan Relay**        | VCC             | 5V                     |                                           |
|                      | GND             | GND                    |                                           |
|                      | IN              | GPIO22                 |                                           |
| **Motor Relay**      | VCC             | 5V                     |                                           |
|                      | GND             | GND                    |                                           |
|                      | IN              | GPIO13                 |                                           |
| **LED**              | Anode (+)       | GPIO5 via 220Ω resistor|                                           |
|                      | Cathode (-)     | GND                    |                                           |
| **I2C LCD Display**  | SDA             | GPIO2 (SDA)            |                                           |
|                      | SCL             | GPIO3 (SCL)            |                                           |
|                      | VCC             | 5V                     |                                           |
|                      | GND             | GND                    |                                           |

## Notes
- Ensure all connections are secure to avoid short circuits.
- Use appropriate resistors for LEDs and pull-down configurations.
- Adjust the threshold for the photoresistor in the code as per your environment's lighting conditions.
- Ensure the relays used are suitable for your load requirements.
