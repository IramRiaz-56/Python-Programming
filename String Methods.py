#String Operation Program

text = input("Enter a string: ")

print("\nChoose an operation:")
print("1. Reverse the string")
print("2. Count vowels")
print("3. Check if palindrome")
print("4. Count words")
print("5. Replace a word")

choice = input("Enter your choice (1-5): ")

if choice == '1':
    print("Reversed string:", text[::-1])

elif choice == '2':
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    print("Number of vowels:", count)

elif choice == '3':
    if text == text[::-1]:
        print("It's a palindrome.")
    else:
        print("Not a palindrome.")

elif choice == '4':
    words = text.split()
    print("Word count:", len(words))

elif choice == '5':
    old = input("Enter word to replace: ")
    new = input("Enter new word: ")
    updated = text.replace(old, new)
    print("Updated string:", updated)

else:
    print("Invalid choice!")
