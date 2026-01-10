#List Operation Program with User Input

#Take list input from user
size = int(input("Enter the size of the list: "))
user_list = []

for i in range(size):
    element = input(f"Enter element {i+1}: ")
    user_list.append(element)

print("\nYour List:", user_list)

#Display operation menu
print("\nSelect an operation to perform:")
print("1. Append")
print("2. Insert")
print("3. Remove")
print("4. Pop")
print("5. Sort")
print("6. Reverse")
print("7. Length")
print("8. Display List")

choice = input("Enter your choice (1-8): ")

#Perform selected operation
if choice == '1':
    new_element = input("Enter element to append: ")
    user_list.append(new_element)
elif choice == '2':
    index = int(input("Enter index to insert at: "))
    new_element = input("Enter element to insert: ")
    user_list.insert(index, new_element)
elif choice == '3':
    rem_element = input("Enter element to remove: ")
    if rem_element in user_list:
        user_list.remove(rem_element)
    else:
        print("Element not found.")
elif choice == '4':
    user_list.pop()
elif choice == '5':
    user_list.sort()
elif choice == '6':
    user_list.reverse()
elif choice == '7':
    print("Length of list:", len(user_list))
elif choice == '8':
    print("List:", user_list)
else:
    print("Invalid choice.")

#Final list display
print("\nUpdated List:", user_list)
