#Python program using nested if statements:
#Program to check if a number is positive, and also check if it's even or odd

num = int(input("Enter a number: "))
if num >= 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("It is also even.")
    else:
        print("It is also odd.")
else:
    print("The number is negative.")
