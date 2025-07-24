# MyHiveConnect App Documentation

## App Development

### Using MIT App Inventor

1. **Import Project**
   - Go to https://appinventor.mit.edu/
   - Click "Import project (.aia)"
   - Select the project file
   - The project will be imported and ready for editing

2. **Editing Project**
   - Use the visual blocks interface to modify functionality
   - Save changes regularly
   - Test changes using the emulator or connected device

## App Installation

### APK Installation

> Only For Android Devices 📲

1. **Prepare Device**
   - Go to Settings > Security
   - Enable "Unknown sources" or "Install from unknown sources"
   - This allows installation of apps from outside the Play Store

2. **Install APK**
   - Transfer the APK file to your Android device
   - Open the APK file
   - Follow the installation prompts
   - Allow permissions when requested

## App Usage Guide

### Hardware Connection

1. **Connect ESP32**
   - Use a USB OTG adapter
   - Connect one end to your Android device
   - Connect the other end to the ESP32 USB-C port
   - Ensure a stable connection

### App Operation

1. **Launch App**
   - Open the installed MyHiveConnect app
   - You'll see the main interface

2. **Connect to Device**
   - Look for the connect button in the top right corner
   - Click it to establish USB serial connection
   - Wait for connection confirmation

3. **Using the Interface**
   - **Input Buttons**: 
     - Use these to send commands to the Hive Scale
     - Each button has a specific function
   - **Prompt Area**: 
     - Displays responses from the Hive Scale
     - Shows measurement data and status
   - **Status Indicators**: 
     - Indicate scale name
     - Indicate sensor readings

### Features

1. **Weight Measurement**
   - Real-time weight display
   - Unit conversion options
   - Zero calibration

2. **Environmental Monitoring**
   - Temperature readings
   - Humidity levels

### Troubleshooting

1. **Connection Issues**
   - Check USB OTG adapter
   - Verify ESP32 power
   - Try reconnecting
   - Check permissions

2. **App Crashes**
   - Clear app cache
   - Reinstall the app
   - Check Android version compatibility

3. **Measurement Problems**
   - Verify sensor connections
   - Check calibration
   - Test individual sensors

### Tips

- Keep the USB connection stable during operation
- Regularly backup measurement data
- Keep the app updated with latest features
- Document any custom modifications