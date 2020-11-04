#!/usr/bin/env micropython
import time
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_D
from ev3dev2.button import Button

btn = Button()

tank_pair = MoveTank(OUTPUT_A, OUTPUT_D)


while True:
    if btn.any():
        break

    tank_pair.on(left_speed=10, right_speed=20)
    
    time.sleep(0.05)

tank_pair.off()
