"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """

    for i in range(7):
       if front_is_clear():
           move()
           jump()
       else:
           jump()


def go_down():
    while front_is_clear():
        move()
    turn_left()

def jump():
    while not front_is_clear():
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()

    move()
    turn_left()
    turn_left()
    turn_left()
    go_down()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
