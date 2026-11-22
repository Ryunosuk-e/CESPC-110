child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))


total_children = int(input("How many children are there? "))
total_adults = int(input("How many adults are there? "))


print()

subtotal = (child_meal_price * total_children) + (adult_meal_price * total_adults)

 