#By Josiah
# On raspberry pi 3
# ultrasonic sensor

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

trig=23
echo=24

print("Distance Measuring")
gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)

while True:
 #   gpio.output(trig,False)    #trig low
  #  time.sleep(2)              #delay 2secs

    gpio.output(trig,True)    #trig  high
    time.sleep(0.00001)
    gpio.output(trig,False)   #trig low


    while gpio.input(echo)==0:
        pulse_st= time.time()

    while gpio.input(echo)==1:
        pulse_end=time.time()


    pulse = pulse_end - pulse_st            #get pulse duration

    distance= pulse*17150                   #pulse duration * 17150 =distance
    distance= round(distance,2)             # round to 2 d.p

    if distance >2 and distance <400:
        print("Distance: {}cm  ".format(distance-0.5))
        time.sleep(5)

    else:
        print("Out of range")
        time.sleep(5)

    
