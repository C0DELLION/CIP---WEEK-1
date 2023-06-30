"""
Program: Khansole Academy
--------------------
Write a program that randomly generates a simple addition problem for the user, reads in the answer from the user, and then checks to see if they got it right or wrong.
More specifically, your program should be able to generate simple addition problems that involve adding two 2-digit integers 
(i.e., the numbers 10 through 99). The user should be asked for an answer to the generated problem. 
Your program should determine if the answer was correct or not, and give the user an appropriate message to let them know.
"""

import random

def main():
    print("Khansole Academy")
    num1 = random.randint(10,99)
    num2 = random.randint(10,99)
    
    print("What is "+str(num1)+" + "+str(num2)+"?")
    answer = int(input("Your answer: "))
    if answer == num1 + num2:
        print("Correct!")
    else:
        print("Incorrect. The expected answer is "+str(answer))
    
if __name__ == '__main__':
    main()
