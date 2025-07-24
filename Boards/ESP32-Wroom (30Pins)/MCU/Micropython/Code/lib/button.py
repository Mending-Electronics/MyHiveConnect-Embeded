import machine
import time
import sys

from machine import Pin

#Import library form "lib" folder
sys.path
['0:/', '0:/lib']
import blinking


### Boot BTN
# Define the GPIO pin connected to the BOOT button
#boot_btn = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
# Define the function to execute when the BOOT button is pressed

#def boot_btn_pressed(pin):
    # Your function code here
#    pass

# Attach an interrupt to the BOOT button
#boot_btn.irq(trigger=machine.Pin.IRQ_FALLING, handler=boot_btn_pressed)


### SERIAL USB BTN
def usb_btn_pressed(pin):
    #USB INIT - Blink led 2 time (1sec)
    blinking.usb_init()
    
    try:
        uart_usb.usb_starter()
        blinking.disconect()
        return
    except:
        import uart_usb
        uart_usb.usb_starter()
        blinking.disconect()
        return

btn_init_usb = machine.Pin(32, machine.Pin.IN, machine.Pin.PULL_UP)
btn_init_usb.irq(trigger=machine.Pin.IRQ_FALLING, handler=usb_btn_pressed)



### SERIAL BLUETOOTH BTN
#def ble_btn_pressed(pin):
#    import uart_bluetooth_le
    
    #Blink led 3 time (0.5 sec)
#    blinking.ble_init()

#btn_init_bluetooth = machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP)
#btn_init_bluetooth.irq(trigger=machine.Pin.IRQ_FALLING, handler=ble_btn_pressed)

