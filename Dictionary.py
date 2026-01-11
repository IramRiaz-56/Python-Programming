'''
Dictionary in Python:
A dictionary is a collection of key-value pairs in Python.  
It is unordered,mutable, and indexed by unique keys (not positions).

Syntax:
my_dict = {
    "name": "Ali",
    "age": 20,
    "city": "Lahore"
}
'''
user_dict = {} #Empty dictionary
#Ask user how many key-value pairs to add
n = int(input("How many entries do you want to add in the dictionary? "))
for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for '{key}': ")
    user_dict[key] = value

#Display final dictionary
print("\nYour Dictionary:")
for k, v in user_dict.items():
    print(f"{k}: {v}")
