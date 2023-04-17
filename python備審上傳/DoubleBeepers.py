"""
File: DoubleBeepers.py
Name:
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        go_back()
    move()
    turn_left()
    turn_left()
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        go_back()

def go_back():
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()






# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
