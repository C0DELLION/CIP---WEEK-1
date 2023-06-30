from karel.stanfordkarel import *

def main():
    #walk along the row till Karel meets the beeper
    while front_is_clear():
        move()
        if beepers_present():    
            build_hospital()
    
def build_hospital():
    #build first column of the hospital building
    turn_left()
    move()
    put_beeper()
    move()
    turn_right()
    put_beeper()
    
    #build second column of the hospital building
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    move()
    turn_left()
    put_beeper()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()
