#!/usr/bin/env micropython
from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep

us = UltrasonicSensor()

while True:

    print("Distance (cm): {:.2f}", us.distance_centimeters)
    sleep(0.5)
