print()
print("Welcome to the Shopping Cart Program! ")
print()


user_action = ""
cart = []

while user_action != "5":

    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    user_action = input("Please enter an action: ")

    if user_action == "1":
        item_to_add = input("What item would you like to add? ").lower()
        cart.append(item_to_add)
        print(f"'{item_to_add}' has been added to the cart.")
        print()
    
    elif user_action == "2":
        print("The contents of the shopping cart are: ")
        for item in cart:
            print(item)
        print()

    elif user_action == "5":
        print("Thank you. Goodbye.")
        break

    else:
        print("Sorry, that is not a valid item number.")
        print()


