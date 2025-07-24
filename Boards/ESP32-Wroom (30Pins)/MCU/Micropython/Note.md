# MicroPython Setup Guide

## Required Software

1. **Thonny IDE**
   - Download from: https://thonny.org/
   - Install the latest version
   - Thonny is a beginner-friendly IDE for MicroPython development

2. **USB Serial Driver**
   - For CH340 or CP210x based boards:
     - Download the Drivers from this repository stored in `Driver` folder 
     - Run the installer and follow the prompts
   - For other USB-to-Serial converters:
     - Install the appropriate driver from the manufacturer's website

## ESP32 Firmware Installation

1. **Prepare the ESP32**
   - Connect the ESP32 to your computer via USB
   - Ensure the USB Serial driver is properly installed

2. **Flash MicroPython Firmware**
   - Use the firmware stored in `Firmware` folder 
   - Or download the latest ESP32 MicroPython firmware from:
     - https://micropython.org/download/esp32/
   - Use Thonny flash tool to flash the firmware
   - Or use esptool.py to flash the firmware:
     ```bash
     esptool.py --chip esp32 --port COMx --baud 115200 erase_flash
     esptool.py --chip esp32 --port COMx --baud 115200 write_flash -z 0x1000 esp32-20230525-v1.21.0.bin
     ```
     - Replace COMx with your actual port number
   

## Project Setup in Thonny

1. **Configure Thonny**
   - Open Thonny IDE
   - Go to Tools > Options > Interpreter
   - Select "MicroPython (ESP32)"
   - Choose the correct COM port

2. **Upload Project Files**
   - Copy your project files to the ESP32:
     - Click "Files" tab in Thonny
     - Click "Upload..." button
     - Select your project files
     - The files will be uploaded to the ESP32's filesystem

3. **Run the Code**
   - Click the "Run" button (green play icon)
   - Or press F5
   - The code will be executed on the ESP32

## Troubleshooting

- If you can't connect to the board:
  - Check USB connection
  - Verify COM port in Thonny settings
  - Try different USB port
  - Ensure USB Serial driver is installed

- If flashing fails:
  - Ensure board is in bootloader mode
  - Check COM port permissions
  - Try different baud rate (921600)

## Tips

- Always backup your code before flashing new firmware
- Keep a copy of working firmware
- Use descriptive filenames for different versions
- Document any custom modifications
