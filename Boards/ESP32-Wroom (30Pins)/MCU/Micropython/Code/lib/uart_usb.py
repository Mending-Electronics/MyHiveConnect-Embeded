import time
import sys

#Import library form "cfg" folder
sys.path.append('/cfg')
sys.path
['0:/', '0:/cfg']
from _serial import serial
from _ratio import ratio, old_average_weighless_value



def usb_calibration():
    
    global ratio, old_average_weighless_value
    
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
            
        print(f"\nThe new ratio was sussefully patched in _ratio.py")
        print(f"The new average weighless value was sussefully patched in _ratio.py\n")
        return new_ratio, new_average_weighless_value
    
    from machine import Pin
    from hx711 import HX711

    from machine import freq

    hx = HX711(d_out=17, pd_sck=4)
    
    print("************************************")
    print("current ratio                   : " + str(ratio))
    print("current average weighless value : " + str(old_average_weighless_value))
    print("************************************")
    
    print("We will start the calibration !\n")

    print("1) Disconnect the internal temperature sensor connector.")
    print("2) Remove the hive and all elements from the scale.")
    print("3) Send 'next' to continue.")
    
    
    while True:
        usb_input = str(input(""))
        # Remove all whitespace characters from a string
        usb_input = "".join(usb_input.split())
    
        if usb_input == "next":
        
            print("\nPlease wait 5 seconds to obtain and average of the empty value.\n")
            
            empty_weight_data = []
            i = 0
            while i < 5:
                empty = hx.read()
                empty_weight_data.append(empty)
                time.sleep_ms(1000)
                i += 1

            new_average_weighless_value = sum(empty_weight_data) / len(empty_weight_data)

            print(f"Data aquired : {empty_weight_data}")
            print(f"New average weighless value : {new_average_weighless_value}\n")
            
            break
            
        elif usb_input == "stop":
            print("-- return in the main program --")
            return
        else:
            print("-- this answer was not emplemented --")
            print("> send : 'next' to continue")
            print("> send : 'stop' to return in the main program")
    

    print("4) Place a plank on the scale to cover the four sensors.")
    print("Send 'next' to continue.")
    

    
    while True:
        usb_input = str(input(""))
        # Remove all whitespace characters from a string
        usb_input = "".join(usb_input.split())
    
        if usb_input == "next":
            tare = hx.read()
            print(f'\nTare value : {tare}')
            print("\nThe tare was successfully done.\n")
            
            break
        
        elif usb_input == "stop":
            print("-- return in the main program --")
            return
        else:
            print("-- this answer was not emplemented --")
            print("> send : 'next' to continue")
            print("> send : 'stop' to return in the main program")
        
    
        
    
    print("5) Place a known weight on the plank")
    print("6) Send the value of the known weight in grams: ")
    print("e.g for 5.26Kg / send : 5260")
    
    
    usb_input = str(input(""))
    # Remove all whitespace characters from a string
    usb_input = "".join(usb_input.split())

    try:

        testWeight = int(usb_input)
        testWeightRead = hx.read()
        # print(testWeightRead)

        new_ratio = (tare - testWeightRead) / testWeight
        
        print(f"New ratio : {ratio}\n")
        #print( f'The weight of 1g is equal to a difference of {round(ratio)} read by the HX711 amplifier')
        
    
    except ValueError:
        print("-- Something wrong --")
        print("6) Send the value of the known weight in grams: ")
        print("e.g for 5.26Kg / send : 5260")
        
    
    edit_ratio(new_ratio, new_average_weighless_value)
        
    
    print("\n************************************")
    print("old ratio                   : " + str(ratio))
    print("old average weighless value : " + str(old_average_weighless_value))
    print("************************************")
    print("new ratio                   : " + str(new_ratio))
    print("new average weighless value : " + str(new_average_weighless_value))
    print("************************************")
    
    # Print the Scale serial number
    print("\n************************************")
    print("Scale : Testing mode")
    print("************************************")
    
    print("\n> send : 'test' to return the current weight in Kg")
    print("> send : 'stop' to return in the main program")
    
    while True:
        usb_input = str(input(""))
        # Remove all whitespace characters from a string
        usb_input = "".join(usb_input.split())

        if usb_input == "stop":
            print("\n-- return in the main program --\n")
            return

        print("\nPlease wait 5 seconds to obtain and average of the current weight value.\n")
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

        print(f'The current weight is : {rounded_value} Kg')





def usb_test():
    while True:
    
       
        # Get the External Temp. and Humidity of the Hive
        try:
            extSensor.measure()
            extTemp = extSensor.temperature()
            extHum = extSensor.humidity()
        except:
            external_sensor = 'Failed to read the exteral sensor.\n'
            
        
        
        # Get the Internal Temp. and Humidity of the Hive
        try:
            
            intSensor.measure()
            currentRead_Temp = intSensor.temperature()
            currentRead_Hum = intSensor.humidity()
        except:
            internal_sensor = 'Failed to read the internal sensor.\n'
        
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
            
            if rounded_value < 25:
                scale_sensor = """
                Something wrong ? The weight is currently under 25Kg.
                > If it's the real current weight on the scale, disregard this warning.
                > If this is not the case:')
                 - The ratio is not correct. Execute the calibration process.
                 - The amplifier work fine, but a load cells sensors can be unconnect.
               Execute a maintenance to reconnect or change the load cell sensor.\n
                """
        except:
            scale_sensor = 'Failed to read the scale sensor.\n'
            



        print("\n************************************")
        print("             TROUBLESHOT             ")
        print("************************************\n\n")
        
        print(external_sensor)
        print(intyernal_sensor)
        print(scale_sensor)





def usb_starter():

    # Print the Scale serial number
    print("************************************")
    print("Serial : " + serial)
    print("************************************")

    # Ask between Testing or Scale Calibration
    print("-- Hi, What do you want to do ? ---")
    print("")
    print("- Send 'test' to start a test.")
    print("- Send 'cal' to start the scale calibration")

    usb_input = str(input(""))
    # Remove all whitespace characters from a string
    usb_input = "".join(usb_input.split())
        
    if usb_input == 'test':
        #usb_test()
        print("test is not implemented")

    elif usb_input == 'cal':
        usb_calibration()

    else:
        pass
