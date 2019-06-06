import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

red=6;
green=13
blue=19
a=[red,green,blue]
b=["Red","Green","Blue"]

gpio.setup(red,gpio.OUT)
gpio.setup(green,gpio.OUT)
gpio.setup(blue,gpio.OUT)


for (pin,col) in zip(a,b):  # iterate through two lists
    
    print("{} led on".format(col))
    gpio.output(pin,True)
    time.sleep(5)
    print("{} led off".format(col))
    gpio.output(pin,False)
    time.sleep(4)


print("Switching all leds on simultanuoesly")
gpio.output(a,True)
time.sleep(5)
print("All leds off")
gpio.output(a,False)

    
    
