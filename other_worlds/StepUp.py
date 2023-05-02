"""
Dildo
File: PotholeFilling.kwld
------------------------
Name: Dildo
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
I want to make love with you.
"""

from karel.stanfordkarel import *


def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_99_beeper()
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












# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
