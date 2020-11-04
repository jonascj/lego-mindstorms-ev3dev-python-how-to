#!/usr/bin/env micropython
import time
from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_D
from ev3dev2.button import Button

btn = Button()

steer_pair = MoveSteering(OUTPUT_A, OUTPUT_D)


while True:
    if btn.any():
        break

    steer_pair.on(steering=-20, speed=10)
    
    time.sleep(0.05)

steer_pair.off()
