'''
For Loop in Python

A for loop is used to iterate over a sequence like a list,
string, or a range of numbers.

Syntax:
for variable in sequence:
    # code block
'''

#Example Program: 
print("Program using For Loop")

#Ask user for a number
num = int(input("Enter a number to print up to: "))

# using for loop
print(f"Numbers from 1 to {num}:")
for i in range(1, num + 1):
    print(i)
