#Import embeded function
import bluetooth
import machine
from machine import Pin, freq
import time

#Import library HX711 and initialize module
from hx711 import HX711
hx = HX711(d_out=17, pd_sck=4)
    
#Import library form "lib" folder
import sys
sys.path
['0:/', '0:/lib']

from ble_uart_peripheral import BLEUART
import blinking


# Create BLE object
ble = bluetooth.BLE()
# Open UART session for BLE
uart = BLEUART(ble)


#Import library form "cfg" folder
sys.path.append('/cfg')
sys.path
['0:/', '0:/cfg']
from _serial import serial
from _ratio import ratio, old_average_weighless_value


# Change the ratio and the average_weighless_value in _ratio.py after the calibration
def edit_ratio(new_ratio, new_average_weighless_value):
    
    import os

    # Set the path to the /cfg folder
    path = "/cfg"

    # Set the filename
    filename = "cfg/_ratio.py"

    ratio = new_ratio
    with open(filename, 'w') as f:
        f.write('ratio = {}'.format(new_ratio))
        f.write('\n')
        f.write('old_average_weighless_value = {}'.format(new_average_weighless_value))
        
    uart.write(f"\nThe new ratio was sussefully patched in _ratio.py")
    uart.write(f"The new average weighless value was sussefully patched in _ratio.py\n")
    return new_ratio, new_average_weighless_value



def ble_calibration():
    
    print('tadaaaa')
    
    global hx
    
    try:
         uart.write("\nPlease wait 5 seconds to obtain and average of the empty value.\n")
    except:
        print('uart not implmented')
    
    
    uart.write("\n************************************")
    uart.write("\ncurrent ratio                   : " + str(ratio))
    uart.write("\ncurrent average weighless value : " + str(old_average_weighless_value))
    uart.write("\n************************************")
    
    uart.write("\nWe will start the calibration !\n")

    uart.write("\n1) Disconnect the internal temperature sensor connector.")
    uart.write("\n2) Remove the hive and all elements from the scale.")
    uart.write("\n3) Send 'next' to continue.\n")
 
   
    while True:
        # Read UART received string 
        uart_in = uart.read() # lire le message recu du Smartphone via Bluetooth
        ble_input = str(uart_in.decode())
        # Remove all whitespace characters from a string
        ble_input = "".join(ble_input.split())
    
    
        if ble_input == "next":
            # Reset ble_input to stop the script
            ble_input=""
            
            uart.write("\nPlease wait 5 seconds to obtain and average of the empty value.\n")
            
            empty_weight_data = []
            i = 0
            while i < 5:
                empty = hx.read()
                empty_weight_data.append(empty)
                time.sleep_ms(1000)
                i += 1

            new_average_weighless_value = sum(empty_weight_data) / len(empty_weight_data)

            uart.write(f"\nData aquired : {empty_weight_data}")
            uart.write(f"\nNew average weighless value : {new_average_weighless_value}\n")
            
            break
            
        elif ble_input == "stop":
            uart.write("\n-- return in the main program --")
            
        else:
            uart.write("\n-- this answer was not emplemented --")
            uart.write("\n> send : 'next' to continue")
            uart.write("\n> send : 'stop' to return in the main program")
    

    uart.write("\n4) Place a plank on the scale to cover the four sensors.")
    uart.write("\nSend 'next' to continue.\n")
    
    
    
    while True:
        # Read UART received string 
        uart_in = uart.read() # lire le message recu du Smartphone via Bluetooth
        ble_input = str(uart_in.decode())
        # Remove all whitespace characters from a string
        ble_input = "".join(ble_input.split())
    
        if ble_input == "next":
            
            # Reset ble_input to stop the script
            ble_input=""
            
            tare = hx.read()
            uart.write(f'\nTare value : {tare}')
            uart.write("\nThe tare was successfully done.\n")
            
            break
        
        elif ble_input == "stop":
            uart.write("\n-- return in the main program --")
            
        
        else:
            uart.write("\n-- this answer was not emplemented --")
            uart.write("\n> send : 'next' to continue")
            uart.write("\n> send : 'stop' to return in the main program")
        
    
        
    
    uart.write("\n5) Place a known weight on the plank")
    uart.write("\n6) Send the value of the known weight in grams: ")
    uart.write("\ne.g for 5.26Kg / send : 5260\n")
    
    
    # Read UART received string 
    uart_in = uart.read() # lire le message recu du Smartphone via Bluetooth
    ble_input = str(uart_in.decode())
    # Remove all whitespace characters from a string
    ble_input = "".join(ble_input.split())

    try:
        testWeight = int(ble_input)
        testWeightRead = hx.read()
        # print(testWeightRead)

        new_ratio = (tare - testWeightRead) / testWeight
        
        uart.write(f"\nNew ratio : {ratio}\n")
        #print( f'The weight of 1g is equal to a difference of {round(ratio)} read by the HX711 amplifier')
        
    
    except ValueError:
        uart.write("\n-- Something wrong --")
        uart.write("\n6) Send the value of the known weight in grams: ")
        uart.write("\ne.g for 5.26Kg / send : 5260")
        
    
    edit_ratio(new_ratio, new_average_weighless_value)
        
    
    uart.write("\n\n************************************")
    uart.write("\nold ratio                   : " + str(ratio))
    uart.write("\nold average weighless value : " + str(old_average_weighless_value))
    uart.write("\n************************************")
    uart.write("\nnew ratio                   : " + str(new_ratio))
    uart.write("\nnew average weighless value : " + str(new_average_weighless_value))
    uart.write("\n************************************")
    
    # Print the Scale serial number
    uart.write("\n\n************************************")
    uart.write("\nScale : Testing mode")
    uart.write("\n************************************")
    
    uart.write("\n\n> send : 'test' to return the current weight in Kg")
    uart.write("\n> send : 'stop' to return in the main program\n")
    
    while True:
        # Read UART received string 
        uart_in = uart.read() # lire le message recu du Smartphone via Bluetooth
        ble_input = str(uart_in.decode())
        # Remove all whitespace characters from a string
        ble_input = "".join(ble_input.split())

        if ble_input == "stop":
            uart.write("\n\n-- return in the main program --\n")
            uart.write("\n\n-- disconnection ---\n")
            uart.close()
            

        uart.write("\n\nPlease wait 5 seconds to obtain and average of the current weight value.\n")
        weight_data = []
        i = 0
        while i < 5:
            currentRead = hx.read()
            weight_data.append(currentRead)
            time.sleep_ms(1000)
            i += 1

        avgWeightValue = sum(weight_data) / len(weight_data)

        current_value_in_grams = (new_average_weighless_value - avgWeightValue) / ratio
        current_value_in_kilograms = current_value_in_grams / 1000
        rounded_value = round(current_value_in_kilograms, 2)

        uart.write(f'\nThe current weight is : {rounded_value} Kg')




def test():
    
    print("ask: ", ask) # afficher le message recu du Smartphone sur le console de Thonny
        
    uart.write(f"\nask: {ask}\n")

    # Header Menue
    if ask == 0 and ble_input != '':
        # Print the Scale serial number
        uart.write("\n************************************")
        uart.write("\nSerial : " + serial)
        uart.write("\n************************************")

        # Ask between Testing or Scale Calibration
        uart.write("\n-- Hi, What do you want to do ? ---\n")
        uart.write("\n- Send 'test' to start a test.")
        uart.write("\n- Send 'cal' to start the scale calibration\n")
        
        ask = 1
        ble_input = ''


    # Calibration
    # ---------------------------
    elif ask == 1 and ble_input == 'cal':
        
        try:
            uart.write("\nPlease wait 5 seconds to obtain and average of the empty value.\n")
        except:
            print('uart not implmented')
        
        
        uart.write("\n************************************")
        uart.write("\ncurrent ratio                   : " + str(ratio))
        uart.write("\ncurrent average weighless value : " + str(old_average_weighless_value))
        uart.write("\n************************************")
        
        uart.write("\nWe will start the calibration !\n")

        uart.write("\n1) Disconnect the internal temperature sensor connector.")
        uart.write("\n2) Remove the hive and all elements from the scale.")
        uart.write("\n3) Send 'next' to continue.\n")
        
        ask = 101
        ble_input = ''
        

    elif ask == 101 and ble_input == 'next':
        uart.write("\nPlease wait 5 seconds to obtain and average of the empty value.\n")
        
        empty_weight_data = []
        i = 0
        while i < 5:
            empty = hx.read()
            empty_weight_data.append(empty)
            time.sleep_ms(1000)
            i += 1

        new_average_weighless_value = sum(empty_weight_data) / len(empty_weight_data)

        uart.write(f"\nData aquired : {empty_weight_data}")
        uart.write(f"\nNew average weighless value : {new_average_weighless_value}\n")
        
        ask = 102
        ble_input = ''
        
    elif ask == 101 and ble_input == "stop":
        uart.write("\n-- return in the main program --")
        ask = 0
        ble_input = ''
        uart.close()
        
    elif ask == 101 and ble_input != "next" and ble_input != "stop"and ble_input != '':
        uart.write("\n-- this answer was not emplemented --")
        uart.write("\n> send : 'next' to continue")
        uart.write("\n> send : 'stop' to return in the main program")







    # Testing
    # ---------------------------   
        
    elif ask == 1 and ble_input == 'test':
        uart.write("\nTesting is not currently implemented")
        pass 

    else:
        pass



# Define ISR for an UART input on BLE connection
def ble_rx():
    
    # Read UART received string 
    uart_in = uart.read() # lire le message recu du Smartphone via Bluetooth
    ble_input = str(uart_in.decode())
    # Remove all whitespace characters from a string
    ble_input = "".join(ble_input.split())
    
    print("UART IN: ", ble_input) # afficher le message recu du Smartphone sur le console de Thonny
    
    uart.write(f"\nUART IN: {ble_input}\n")
    
    test()





ask = 0       
ble_input = ''

# Map ISR to UART read interrupt
uart.irq(handler=ble_rx)

print("ask: ", ask) # afficher le message recu du Smartphone sur le console de Thonny
    
uart.write(f"\nask: {ask}\n")

# Header Menue
if ask == 0 and ble_input != '':
    # Print the Scale serial number
    uart.write("\n************************************")
    uart.write("\nSerial : " + serial)
    uart.write("\n************************************")

    # Ask between Testing or Scale Calibration
    uart.write("\n-- Hi, What do you want to do ? ---\n")
    uart.write("\n- Send 'test' to start a test.")
    uart.write("\n- Send 'cal' to start the scale calibration\n")
    
    ask = 1
    ble_input = ''


# Calibration
# ---------------------------
elif ask == 1 and ble_input == 'cal':
    
    try:
        uart.write("\nPlease wait 5 seconds to obtain and average of the empty value.\n")
    except:
        print('uart not implmented')
    
    
    uart.write("\n************************************")
    uart.write("\ncurrent ratio                   : " + str(ratio))
    uart.write("\ncurrent average weighless value : " + str(old_average_weighless_value))
    uart.write("\n************************************")
    
    uart.write("\nWe will start the calibration !\n")

    uart.write("\n1) Disconnect the internal temperature sensor connector.")
    uart.write("\n2) Remove the hive and all elements from the scale.")
    uart.write("\n3) Send 'next' to continue.\n")
    
    ask = 101
    ble_input = ''
    

elif ask == 101 and ble_input == 'next':
    uart.write("\nPlease wait 5 seconds to obtain and average of the empty value.\n")
    
    empty_weight_data = []
    i = 0
    while i < 5:
        empty = hx.read()
        empty_weight_data.append(empty)
        time.sleep_ms(1000)
        i += 1

    new_average_weighless_value = sum(empty_weight_data) / len(empty_weight_data)

    uart.write(f"\nData aquired : {empty_weight_data}")
    uart.write(f"\nNew average weighless value : {new_average_weighless_value}\n")
    
    ask = 102
    ble_input = ''
    
elif ask == 101 and ble_input == "stop":
    uart.write("\n-- return in the main program --")
    ask = 0
    ble_input = ''
    uart.close()
    
elif ask == 101 and ble_input != "next" and ble_input != "stop"and ble_input != '':
    uart.write("\n-- this answer was not emplemented --")
    uart.write("\n> send : 'next' to continue")
    uart.write("\n> send : 'stop' to return in the main program")







# Testing
# ---------------------------   
    
elif ask == 1 and ble_input == 'test':
    uart.write("\nTesting is not currently implemented")
    pass 

else:
    pass
        
        





