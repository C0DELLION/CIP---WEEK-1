from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers infinite
her bag. 
"""

def main():
    move()
    check_rows()
    
#pre conditions : Karel facing East, there are 4 beepers on 2nd collumn
#post conditions : Beepers move on every each collumn, Karel back home facing East, 2nd column only has 1 beeper

def check_rows():
    
    while beepers_present():
        pick_beeper()
        
        # check the next column to find empty spaces to put beepers
        if beepers_present():
            while beepers_present():
                move()
                
            put_beeper()
            move_to_next_column()
        else:
            put_beeper()
            back_home()

def move_to_next_column():
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    move()
    
def turn_around():
    turn_left()
    turn_left()
    
def back_home():
    turn_around()
    move()
    turn_around()

if __name__ == '__main__':
    main()
