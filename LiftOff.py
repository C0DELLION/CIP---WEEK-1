"""
Program: Liftoff
--------------------
Write a program that prints out the calls for a spaceship that is about to launch. 
Countdown from 10 to 1 and then output Liftoff!
"""

def main():
    for i in range(1,11)[::-1]:
        print(i) 
    print("Liftoff!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
