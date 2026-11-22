# Note addition to list of initial options. I added an option to check out all items added so far, 
# enabling user to calculate the sales tax, find out total amount to pay, pay and recieve change if available 
print()
print("Welcome to the Shopping Cart Program! ")
print()


user_action = ""
cart = []
price_list = []

while user_action != "6":

    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Checkout")
    print("6. Quit")
    print()

    user_action = input("Please enter an action: ")

    if user_action == "1":
        item_to_add = input("What item would you like to add? ").capitalize()
        cart.append(item_to_add)
        price_of_item = float(input(f"What is the price of '{item_to_add}' "))
        price_list.append(price_of_item)
        print(f"'{item_to_add}' has been added to the cart.")
        print()
    
    elif user_action == "2":
        print("The contents of the shopping cart are: ")
        # for item in cart:
        #     print(item)
        for i in range(len(cart)):
            item = cart[i]
            price = price_list[i]
            human_count = i + 1
            print(f"{human_count}. {item} - ${price:.2f}")
        print()

    elif user_action == "3":
        human_item_to_remove = int(input("Which item would you like to remove? "))
        item_to_remove = human_item_to_remove - 1
        if item_to_remove <= len(cart) :
            cart.pop(item_to_remove)
            price_list.pop(item_to_remove)
            print(f"Item '{human_item_to_remove}' has been removed.")
            print()
        else:
            print("Sorry, that is not a valid item number.")
            print()

    elif user_action == "4":
        total_price = 0
        for price in price_list:
            total_price = total_price + price
        print(f"The total price of the items in the shopping cart is ${total_price:.2f}")
        print()

    elif user_action == "5":
        print(f"You're about to checkout items in the shopping cart worth ${total_price:.2f}")
        print()
        sales_tax_rate = float(input("What is the sales tax rate? "))
        sales_tax_rate_percent = sales_tax_rate / 100
        sales_tax = sales_tax_rate_percent * total_price
        print(f"Sales Tax: ${sales_tax:.2f}") 

        total_amount = total_price + sales_tax
        print(f"Total: ${total_amount:.2f}")

        print()

        payment_amount = float(input("What is the payment amount? "))
        change = payment_amount  - total_amount
        print(f"Payment of ${total_amount:.2f} Sucessful!")
        print(f"Change: ${change:.2f}")

    elif user_action == "6":
        print("Thank you. Goodbye.")
        print()
        break

    else:
        print("Sorry, that is not a valid item number.")
        print()


