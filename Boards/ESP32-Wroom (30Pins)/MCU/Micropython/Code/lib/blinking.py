from machine import Pin
import time

def usb_init():
    
    ledBuitIn = Pin(2, Pin.OUT)    # create output pin on GPIO0
    for i in range(2):
        ledBuitIn.on()             # set pin to "on" (high) level
        time.sleep(1)              # sleep for 1 second
        ledBuitIn.off()            # set pin to "off" (low) level
        time.sleep(1)              # sleep for 1 second

def ble_init():
    ledBuitIn = Pin(2, Pin.OUT)    # create output pin on GPIO0
    
    for i in range(3):
        ledBuitIn.on()             # set pin to "on" (high) level
        time.sleep(0.5)              # sleep for 1 second
        ledBuitIn.off()            # set pin to "off" (low) level
        time.sleep(0.5)              # sleep for 1 second


def receive():
    ledBuitIn = Pin(2, Pin.OUT)    # create output pin on GPIO0
    ledBuitIn.on()             # set pin to "on" (high) level
    time.sleep(0.5)              # sleep for 1 second
    ledBuitIn.off()            # set pin to "off" (low) level


def disconect():
    ledBuitIn = Pin(2, Pin.OUT)    # create output pin on GPIO0
    ledBuitIn.on()             # set pin to "on" (high) level
    time.sleep(2)              # sleep for 1 second
    ledBuitIn.off()            # set pin to "off" (low) level

