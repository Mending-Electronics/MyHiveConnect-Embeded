
from machine import Pin
from hx711 import HX711

import time

from machine import freq

hx = HX711(d_out=5, pd_sck=4)

print("Please remove all elements on the scale and send 'next' to continue.")
input()
print("Please wait 5 seconds to obtain and average of the empty value.")
emptyWeightData = []
i = 0
while i < 5:
    empty = hx.read()
    emptyWeightData.append(empty)
    time.sleep_ms(1000)
    i += 1

avgEmptyWeightValue = sum(emptyWeightData) / len(emptyWeightData)

print(emptyWeightData)
print(avgEmptyWeightValue)



print("Please place a plank on the scale and send 'next' to continue.")
input()
tare = hx.read()
print(tare)

print("The tare was successfully done.")
print("Please place a known weight on the plank and send 'next' to continue.")
input()
testWeight = int(input("Please enter the value of the known weight in grams: "))
testWeightRead = hx.read()
print(testWeightRead)



ratio = (tare - testWeightRead) / testWeight
print( f'The weight of 1g is equal to a difference of {round(ratio)} read by the HX711 amplifier')

while True:
    weightData = []
    i = 0
    while i < 3:
        currentRead = hx.read()
        weightData.append(currentRead)
        time.sleep_ms(1000)
        i += 1

    avgWeightValue = sum(weightData) / len(weightData)

    current_value_in_grams = (avgEmptyWeightValue - avgWeightValue) / ratio
    current_value_in_kilograms = current_value_in_grams / 1000
    rounded_value = round(current_value_in_kilograms, 2)
    
    print(f'The current weight is : {rounded_value} Kg')
