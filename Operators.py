#Python: Arithmetic & Logical Operators
'''
➤ Arithmetic Operators
Used to perform basic mathematical operations:

| Operator | Description        | 
|----------|----------------- --|
|   +      | Addition           | 
|   -      | Subtraction        | 
|   *      | Multiplication     | 
|   /      | Division (float)   | 
|   //     | Floor Division     | 
|   %      | Modulus (remainder)| 
|   *      | Exponentiation     | 
'''
#Example:
print("Example of Arithmetic Operators:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b) 
print("Remainder:", a % b)  
'''
➤ Logical Operators
Used for making decisions based on conditions:

| Operator | Description            | Example               | Output |
|----------|------------------------|-----------------------|--------|
| and      | True if both are True  | True and False        | False  |
| or       |  True if one is True   | True or False         | True   |
| not      | Reverses the result    | not(True)             | False  |
'''
#Example:
x = int(input("Enter a number: "))
print("Checking if number is between 2 and 10:")
print(x > 2 and x < 10)
