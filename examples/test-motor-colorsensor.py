#!/usr/bin/env micropython

from ev3dev2.motor import LargeMotor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button

btn = Button()

ma = LargeMotor('outA')
mb = LargeMotor('outD')

cl = ColorSensor()
cl.mode='COL-AMBIENT'
while True:
    if btn.any():
        break

    ma.on(speed=10)
    mb.on(speed=10)
    
    print(cl.value())

ma.off()
mb.off()
