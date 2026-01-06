'''
While Loop in Python
A while loop continues to execute a block of code 
as long as a given condition is true*.

Syntax:
while condition:
    # code block
'''
#Practice Program 
print("program using while loop")

num = int(input("Enter a number to print up to: "))         #Ask user for a number
i = 1                                      #Initialize counter
#Print numbers from 1 to num using while loop
print(f"Numbers from 1 to {num}:")
while i <= num:
    print(i)
    i += 1
