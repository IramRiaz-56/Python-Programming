'''
Conditional Statements
Conditional statements allow a program to take decisions based on certain conditions. 
They are used to execute a block of code only if a specific condition is true.

if Statement
Executes a block of code ifthe condition is true.

Syntax:
if condition:
    # code to execute
#Example:
x = 10
if x > 5:
    print("x is greater than 5")

 if-else Statement
Executes one block if condition is true, otherwise another block.

Syntax:
if condition:
    # code if condition is true
else:
    # code if condition is false

Example:
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

if-elif-else Statement
Checks multiple conditions one by one.

Syntax:
if condition1:
    # code
elif condition2:
    # code
else:
    # code

Example:

x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

Nested if Statements
An if inside another if.
Example:
x = 10
if x > 0:
    if x % 2 == 0:
'''
