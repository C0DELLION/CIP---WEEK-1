"""
Program: Random Numbers!
--------------------
This program prints out 10 random numbers in the range 1 to 100, inclusive.
"""

# this is necessary if you want to use random numbers
import random

def main():
    for i in range(10):
    # generate random number between min 1 and max 100
        value = random.randint(1, 100)
        print(value)

if __name__ == '__main__':
    main()
