# 🐝 MyHiveConnect - Embedded & Mobile

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Tech: MicroPython](https://img.shields.io/badge/Tech-MicroPython-green.svg)
![Device: ESP32 Wroom 30Pin](https://img.shields.io/badge/Hardware-ESP32--Wroom--30Pin-blue.svg)
![Mobile: MIT App Inventor](https://img.shields.io/badge/MobileApp-No--Code--MIT%20App%20Inventor-purple.svg)

## 🌟 Project Overview

**MyHiveConnect** is an open-source solution for monitoring beehives using embedded systems and mobile technology. This project provides a complete system for monitoring hive conditions and weight.

## 📋 Project Structure

```
MyHiveConnect-Embeded/
├── .screenshots/       # Project screenshots
├── App/                 # MIT App Inventor source files
├── Boards/             # Hardware configuration files
└── docs/               # Additional documentation
```

## 🧠 System Architecture

- 🧭 **Microcontroller**: ESP32-WROOM (30-pin USB-C) with CH340 serial
- 📲 **Mobile App**: Developed with MIT App Inventor
- 🔌 **Connection**: USB OTG between ESP32 and Android device
- ⚡ **Power System**: Solar panel (20W 5V) and Li-ion battery

## 📊 Core Features

- 📈 Weight measurement (4x 50kg load cells)
- 🌡️ Temperature monitoring
- 💧 Humidity monitoring
- ⚡ Solar power management
- 📱 Android app interface
- 🔄 Real-time data updates

## 📸 System Screenshot

![MyHiveConnect Interface](https://raw.githubusercontent.com/Mending-Electronics/MyHiveConnect-Embeded/main/.screenshots/screenshot0001.png)

## 🧰 Hardware Components

| Component                          | Description                                     |
|-----------------------------------|-------------------------------------------------|
| Solar Panel                       | 20W 5V for power generation                    |
| Load Cells                        | 4x 50kg capacity for weight measurement        |
| HX711 Amplifier                   | Load cell signal processing                    |
| AM2301 Sensor                     | Digital Temp/Humidity (waterproof)             |
| DHT22 Module                      | Digital Temp/Humidity                          |
| DC-DC Buck Converter              | 5V to 3.3V for ESP32                          |
| Solar Charge Controller           | Li-ion 3.7V battery management                |
| ESP32-WROOM                       | Main controller (30-pin USB-C)                 |

## 🚀 Future Improvements

- Add BLE wireless communication
- Add a microphone to detect whether the bees are alive
- Add LoRa Transmitter and a Gateway to send data to a remote server
- Add AI-based hive activity analysis

## 📢 License & Contributions

This project is licensed under the **MIT License**. Contributions are welcome!

---

## 📌 Tags

`#OpenSource` `#Beekeeping` `#EmbeddedSystems` `#MicroPython` `#ESP32` `#HiveMonitoring` `#NoCode` `#MITAppInventor` `#IoT` `#AndroidUSBOTG`
