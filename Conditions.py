#!/usr/bin/env pybricks-micropython
#aaahahhhhhhh
"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
#Inizialisar sensor de tacto
left_sensor = TouchSensor(Port.S1)
right_sensor = TouchSensor(Port.S2)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=137)
#robot = DriveBase.Stop()

# Go forward and backwards for one meter.
#left_motor.run_time(-1000, 1000, then=Stop.HOLD, wait=False)
#right_motor.run_time(1000, 1000, then=Stop.HOLD, wait=True)

while True:
    if left_sensor.pressed() or right_sensor.pressed():
        ev3.speaker.beep()
        left_motor.stop()
    else:
        left_motor.run_time(-1000, 1000, then=Stop.HOLD, wait=False)
        right_motor.run_time(1000, 1000, then=Stop.HOLD, wait=True)

#robot.straight(1000)
ev3.speaker.beep()

