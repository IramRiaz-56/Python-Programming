
'''
 Slicing in Python

Slicing means extracting a specific part (subsection) from a sequence 
like a string , list , or tuple using indexes.

Syntax:
sequence[start : end : step]

start : starting index (inclusive)
end: ending index (exclusive)
step: jump (optional)
'''
#String Slicing 

text = input("Enter a string: ") # Get a string input from the user

# Get slicing indexes from the user
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))
step = int(input("Enter step (enter 1 if not sure): "))

sliced_text = text[start:end:step]  # Perform slicing

# Show result
print("Sliced part of string:", sliced_text)
