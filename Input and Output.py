#input / Output in Python
'''
Input:
Used to take data from the user.
Syntax:
variable = input("Enter something: ")
'''
#Example:
print("input example")
name = input("Enter your name: ")
print("Hello", name)

#Note: Input is always taken as string.
'''
Output:
Used to display data to the user.
Syntax:
print(data)
'''
#Example:
print("output example")
age = 20
print("Your age is", age)

#Type Casting
'''       
Type casting* means converting one data type into another.
Common type casting functions:
🔹int() — Converts to integer  
x = int("5")       # string to int
🔹float() — Converts to float  
y = float("3.14")
🔹str() — Converts to string
z = str(100)
'''
print("type casting example")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = int(num1) + int(num2)       #Convert to int before addition
print("Sum is:", sum)
