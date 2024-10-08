# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.

# Task 2: Include a function to remove items from the list.

# Task 3: Add a function that prints out the entire list in a formatted way.

# shopping cart list/choice function
def shopping_menu():
    
    while True:

        print("""
            <<-----Shopping Menu----->>
            1. Add item
            2. Delete Item
            3. View Shopping Cart
            4. Quit
        """)

        option = input("Choose your option: ")

        if option == "1":
            add_item()
        elif option == "2":
            del_item()
        elif option == "3":
            view_cart()
        elif option == "4":
            print("Thank you for shopping at V-Mart!")
            print(*shopping_list, sep = ", ")
            break
        else:
            print("That is not a valid choice!")

shopping_list = []

# add item/price function
def add_item():
    item = input("Add item to your shopping list: ")
    shopping_list.append(item)
    print(f"{item} has been added to your cart.")

# remove item function
def del_item():
    item = input("Remove item from your shopping list: ")
    shopping_list.remove(item)
    print(f"{item} has been removed from your cart.")

# view cart function
def view_cart():
    print(*shopping_list, sep = ", ")


shopping_menu()