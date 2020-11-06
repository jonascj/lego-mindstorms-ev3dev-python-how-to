#!/usr/bin/env micropython
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

cl = ColorSensor() 

input("Place white paper under colorsensor and press [Enter]")
cl.calibrate_white()

while True:
    print("reflected:", cl.reflected_light_intensity)
    sleep(0.2)

    print("ambient:", cl.ambient_light_intensity)
    sleep(0.2)

    r,g,b = cl.rgb
    print( "r: {}, g: {}, b: {}".format(r,g,b) )
    sleep(0.2)
    

