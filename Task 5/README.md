# Smart Elevator Controller Using VSDsquadron Mini
## Overview
Sure! Here’s a simplified version of the smart elevator project using a 16x2 LCD with an I2C interface, a 4x4 keypad, push buttons, and the VSDsquadron Mini board.

### Components Required
1. *VSDsquadron Mini board*
2. *16x2 LCD Display with I2C Module*
3. *4x4 Keypad*
4. *Breadboard and Jumper Wires*
5. *USB Cable for Power and Data*

### Pin Connections
#### LCD with I2C Connections
- *VCC*: Connect to +5V
- *GND*: Connect to GND
- *SDA*: Connect to I2C SDA pin (e.g., GPIO PC1)
- *SCL*: Connect to I2C SCL pin (e.g., GPIO PC2)

#### Keypad Connections
- *Row Pins (R1-R4)*: Connect to GPIO pins D0, D1, D2, D3
- *Column Pins (C1-C4)*: Connect to GPIO pins D4, D5, D6, D7


### Simplified Process

1. *Connect the LCD*:
   - *Power*: VCC to +5V, GND to GND
   - *I2C Data*: SDA to PC1, SCL to PC2

2. *Connect the Keypad*:
   - *Rows*: R1 to D0, R2 to D1, R3 to D2, R4 to D3
   - *Columns*: C1 to D4, C2 to D5, C3 to D6, C4 to D7

3. *Power and Data Connection*:
   - Connect the VSDsquadron Mini board to the computer using a USB cable for both power and data communication.
