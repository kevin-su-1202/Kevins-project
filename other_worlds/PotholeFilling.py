"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    move()
    fill_hole()
    move()
    move()
    fill_hole()
    move()
    move()
    fill_hole()
    spin()
    run()

def put_99_beeper():
    for i in range(99):
        put_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def spin():
    for i in range(100):
        turn_left()


def run():
    for i in range(99):
        move()


def fill_hole():
    turn_right()
    move()
    for i in range(99):
        put_beeper()
    turn_left()
    turn_left()
    move()
    turn_right()





















# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
