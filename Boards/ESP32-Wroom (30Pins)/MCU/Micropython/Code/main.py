from machine import Pin, freq

import time
import sys

import dht
from hx711 import HX711

#Import library form "lib" folder
sys.path
['0:/', '0:/lib']
import button

#Import library form "cfg" folder
sys.path.append('/cfg')
sys.path
['0:/', '0:/cfg']
from _serial import serial
from _ratio import ratio, old_average_weighless_value
from _corrector import corrector_internal_temp, corrector_external_temp, corrector_internal_hum, corrector_external_hum


extSensor = dht.DHT22(Pin(14))
intSensor = dht.DHT22(Pin(21))
hx = HX711(d_out=17, pd_sck=4)

while True:
    

   
    # Get the External Temp. and Humidity of the Hive
    try:
        extSensor.measure()
        extTemp = extSensor.temperature() + corrector_external_temp
        extHum = extSensor.humidity() + corrector_external_hum
        extTemp_f = extTemp * (9/5) + 32.0
    except OSError as e:
        pass
        
    # Get the Internal Temp. and Humidity of the Hive
    try:
        
        internal_temp_data = []
        internal_hum_data = []
        i = 0
        while i < 5:
            intSensor.measure()
            currentRead_Temp = intSensor.temperature()
            currentRead_Hum = intSensor.humidity()
            
            internal_temp_data.append(currentRead_Temp)
            internal_hum_data.append(currentRead_Hum)
            time.sleep_ms(100)
            i += 1

        avg_internal_temp_value = sum(internal_temp_data) / len(internal_temp_data)
        avg_internal_hum_value = sum(internal_hum_data) / len(internal_hum_data)
        
        intTemp = avg_internal_temp_value + corrector_internal_temp
        intHum = avg_internal_hum_value + corrector_internal_hum
        
        #intSensor.measure()
        #intTemp = intSensor.temperature()
        #intHum = intSensor.humidity()
        intTemp_f = intTemp * (9/5) + 32.0
    except OSError as e:
        pass
    
    # Get the Weight of the Hive in Kg     
    try:
        weight_data = []
        i = 0
        while i < 3:
            currentRead = hx.read()
            weight_data.append(currentRead)
            time.sleep_ms(1000)
            i += 1

        avgWeightValue = sum(weight_data) / len(weight_data)

        current_value_in_grams = (old_average_weighless_value - avgWeightValue) / ratio
        current_value_in_kilograms = current_value_in_grams / 1000
        rounded_value = round(current_value_in_kilograms, 2)
    
    except OSError as e:
        pass
    
    
    
    # Print the Scale serial number
    print("************************************")
    print("Serial : " + serial)
    print("************************************")
    
    print("\nold ratio                   : " + str(ratio))
    print("old average weighless value : " + str(old_average_weighless_value))
    print("\n")
    
    try:
        # Print the External Temp. and Humidity of the Hive
        print('External Temperature: %3.1f C' %extTemp)
        print('External Temperature: %3.1f F' %extTemp_f)
        print('External Humidity: %3.1f %%\n' %extHum)
    except:
        print("Something wrong with the External sensor...\n")
    
    try:
        # Print the Internal Temp. and Humidity of the Hive
        print('Internal Temperature: %3.1f C' %intTemp)
        print('Internal Temperature: %3.1f F' %intTemp_f)
        print('Internal Humidity: %3.1f %%\n' %intHum)
    except:
        print("Something wrong with the Internal sensor...\n")
    
    try:
        # Print the Weight of the Hive in Kg 
        print(f'The current weight is : {rounded_value} Kg\n\n')
    except:
        print("Something wrong with the Scale sensor...\n")
    
    time.sleep_ms(1000)
