# 🐝 MyHiveConnect - Embedded & Mobile

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Tech: MicroPython](https://img.shields.io/badge/Tech-MicroPython-green.svg)
![Device: ESP32 Wroom 30Pin](https://img.shields.io/badge/Hardware-ESP32--Wroom--30Pin-blue.svg)
![Mobile: MIT App Inventor](https://img.shields.io/badge/MobileApp-No--Code--MIT%20App%20Inventor-purple.svg)

## 🌟 Project Overview

**MyHiveConnect** is a 100% open-source solution focused on monitoring the vital parameters of beehives.

This GitHub repository is **exclusively dedicated to** the **embedded firmware and mobile application**, offering real-time access to environmental and structural metrics collected inside the hive.

## 🧠 System Architecture

- 🧭 **Microcontroller**: ESP32 Wroom (30-pin) running MicroPython  
- 📲 **Mobile App**: Developed with **MIT App Inventor** using no-code blocks  
- 🔌 **Connection**: USB-C OTG between the hive controller and Android smartphone

## 📊 Core Features

- Internal & external **temperature and humidity** sensors
- Hive **weight monitoring** (max 200 kg) with calibration support
- Integrated **solar panel** for energy autonomy
- Rechargeable **Li-Po battery** for nighttime operation
- **OTG USB-C** communication with Android devices

## 🧰 Hardware Summary

| Component                          | Description                                     |
|-----------------------------------|-------------------------------------------------|
| 🏋️‍♂️ Scale                        | Max load: 200 kg                                |
| 🧪 Calibration                     | Manual/software calibration support             |
| 🌡️ Temp & Humidity Sensors        | Internal & external readings                    |
| ☀️ Solar Panel                     | Sustainable power supply                        |
| 🔋 Li-Po Battery                   | Stores and powers system overnight              |
| 🔌 USB-C OTG                       | Connects hive ESP32 to Android device           |

## 📁 Repository Contents

- `/firmware` – MicroPython code for ESP32 sensors, I/O, and power logic  
- `/app` – MIT App Inventor source and exported `.aia` file  
- `/docs` – Technical documentation and wiring diagrams  

## 🚀 Future Improvements

- Wireless syncing via Bluetooth Low Energy (BLE)
- AI-based hive activity prediction
- Extended sensor support (CO₂, light levels, etc.)

## 📢 License & Contributions

This project is proudly licensed under the **MIT License**, making it freely usable, modifiable, and distributable. Contributions are highly encouraged—join us in building smarter tools for beekeeping!

---

## 📌 Tags

`#OpenSource` `#Beekeeping` `#EmbeddedSystems` `#MicroPython` `#ESP32` `#HiveMonitoring` `#NoCode` `#MITAppInventor` `#IoT` `#AndroidUSBOTG`

