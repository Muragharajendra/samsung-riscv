# 🚀 Smart Elevator System

## Overview

This **Smart Elevator System** is designed to provide multiple ways to control an elevator, including **voice commands, facial recognition, and a 4×4 keypad** for manual operation. The system seamlessly integrates an **ESP8266 module** with a **VSDSquadron Mini** to process and execute floor selection commands.

## Features

✅ Voice Control – Use speech recognition to select a floor, and the command is sent to the ESP8266 for processing.

✅ Facial Recognition – The system identifies registered users and automatically takes them to their preset floor.

✅ Keypad Control – A 4×4 keypad allows manual floor selection for convenience.

✅ Wi-Fi Communication – The ESP8266 handles all communication, sending the floor selection to the VSDSquadron Mini.

✅ LCD Display – Shows real-time status updates like current floor and destination.

✅ 2-Second Floor Transition Delay – Simulates realistic elevator movement.
## How It Works

1. **Registration** – Users can register their name and floor number while the system captures their face data.
2. **Face Recognition** – If a registered user is detected, the system automatically selects their assigned floor.
3. **Voice Commands** – The user speaks their desired floor number, and the system processes it using speech recognition.
4. **Keypad Input** – A 4×4 keypad allows users to manually enter the floor number.
5. **ESP8266 Communication** – The ESP8266 sends the floor selection data to the VSDSquadron Mini.
6. **Elevator Simulation** – The system displays messages like "Going to Floor X" and updates the current floor in real-time.

## Software & Tools Used

- **VS Code** – For coding and debugging.
- **PlatformIO (in VS Code)** – For developing and uploading firmware.
- **Arduino IDE** – For testing ESP8266 communication.
- **OpenCV & face\_recognition (Python)** – For facial recognition.

## Usage

- **Voice Control:** The system listens for voice commands, extracts the floor number, and sends it to the ESP8266 for execution.
- **Facial Recognition:** If a known face is detected, the elevator automatically moves to the stored floor.
- **Keypad Control:** Users can manually select a floor using the 4×4 keypad.
- **Real-time Display:** The LCD shows the selected floor and updates the current position.


##





[#Click for Video Link](https://drive.google.com/file/d/1X0jPFMdjehkbpRif7oJnZ52r4-G-SuPJ/view?usp=sharing)
