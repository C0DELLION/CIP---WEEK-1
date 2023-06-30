from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    column()
    while front_is_clear():
        next_column()
        column()
  
def column():
    #Giving Karel direction to place the beepers
    turn_left()
    while front_is_clear():
        put_beepers()
        move()
    if front_is_blocked():
        put_beepers()
        turn_right()

def turn_right():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    
def next_column():
    #move Karel to columns where the beepers need to be placed
    for i in range(4):
        move()

def put_beepers():
    if beepers_present():
        pass 
    else:
        put_beeper()

if __name__ == '__main__':
    main()
