
# String Operations
'''
A *string* is a sequence of characters enclosed in quotes.
'''         
text = "Hello, Python!"
print("String Example:" , text)
#➤ String Creation
str1 = 'Hello'
str2 = "World"
str3 = '''Multi-line
String'''

'''         
➤ Basic String Operations

| Operation         | Example                   | Output         |
|------------------|-------------------------- -|----------------|
| Concatenation     | "Hello" + "World"         | HelloWorld     |
| Repetition        | "Hi" * 3                  | HiHiHi         |
| Indexing          | "Python"[0]               | P              |
| Slicing           | "Python"[1:4]             | yth            |
| Length            | len("Python")            | 6              |

String Methods

| Method            | Description                             |  
|----------------- -|-----------------------------------------|
|   .lower()        | Converts to lowercase                   | 
|  .upper()         | Converts to uppercase                   | 
|  .strip()         | Removes whitespace                      | 
|  .replace()       | Replaces substring                      |
|  .find()          | Finds substring index                   | 
|  .split()         | Splits into list                        | 
|  .join()          | Joins list to string                    | 

'''    
#➤ String Formatting

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Using Format Method: ")
print(f"My name is {name} and I am {age} years old.")

#➤ Multiline Strings
print("Multiline String Example:")
multiline = """This is
a multiline
string."""
print(multiline)
