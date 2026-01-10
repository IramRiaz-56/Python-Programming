# Set Operation Program with User Input

# Create a set
size = int(input("Enter the number of elements in the set: "))
user_set = set()

for i in range(size):
    element = input(f"Enter element {i+1}: ")
    user_set.add(element)

print("\nYour Set:", user_set)

# Display operation menu
print("\nSelect an operation to perform:")
print("1. Add Element")
print("2. Remove Element")
print("3. Discard Element")
print("4. Pop Element")
print("5. Clear Set")
print("6. Union with Another Set")
print("7. Intersection with Another Set")
print("8. Display Set")

choice = input("Enter your choice (1-8): ")

# Perform operation
if choice == '1':
    new_element = input("Enter element to add: ")
    user_set.add(new_element)
elif choice == '2':
    rem_element = input("Enter element to remove: ")
    if rem_element in user_set:
        user_set.remove(rem_element)
    else:
        print("Element not found.")
elif choice == '3':
    disc_element = input("Enter element to discard: ")
    user_set.discard(disc_element)
elif choice == '4':
    user_set.pop()
elif choice == '5':
    user_set.clear()
elif choice == '6':
    other = set(input("Enter comma-separated elements for second set: ").split(","))
    user_set = user_set.union(other)
elif choice == '7':
    other = set(input("Enter comma-separated elements for second set: ").split(","))
    user_set = user_set.intersection(other)
elif choice == '8':
    print("Set:", user_set)
else:
    print("Invalid choice.")

# Final Set Display
print("\nUpdated Set:", user_set)
