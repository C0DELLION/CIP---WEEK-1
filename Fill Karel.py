from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    # while loop always assumes that karel is facing right (east)
    while front_is_clear():
        fill_row()
        reset_to_next_row()
       
    
def fill_row():
    #checking the rows 
    while front_is_clear():
        fill_column()
        move()
    #fence-post
    fill_column()


def fill_column():
    #fill every spaces of empty column with beepers
    if no_beepers_present():
        put_beeper()
        
    
def reset_to_next_row():
    #Make Karel goes to next row
    #Pre: Karel is at the end of a row, facing right (east)
    #Post: Karel is at the start of the next row, facing right (east)
    #While Karel facing north, n the front is blocked, karen turns right till it hits the wall
    turn_around()
    move_to_wall()
    turn_right()
    
    if front_is_blocked():
            turn_around()
            turn_left()
            while front_is_clear():
                move()
    else:
        move()
        turn_right()
    
def move_to_wall():
    while front_is_clear():
        move()
    
def turn_right():
    for i in range(3):
        turn_left()
        
        
def turn_around():
    turn_left()
    turn_left()
    
if __name__ == '__main__':
    main()
