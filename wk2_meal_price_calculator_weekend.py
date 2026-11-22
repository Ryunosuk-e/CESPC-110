#Note additions on lines 5, 6, 10, 11, and 15. I added an entry for drink price and table price incase the customer want to eat in. then added total for more than one booking, and drink, then calculated the sub total. 

child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
drink_price = float(input("What is the price of a drink? "))
table_price = float(input("What is the price of the table? "))

total_children = int(input("How many children are there? "))
total_adults = int(input("How many adults are there? "))
total_drinks = int(input("How many drinks are there? "))
total_tables = int(input("How many tables were booked? "))

print()

subtotal = (child_meal_price * total_children) + (adult_meal_price * total_adults) + (drink_price * total_drinks) + (table_price * total_tables)
print(f"Subtotal: ${subtotal:.2f}")

print()

sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax_rate_percent = sales_tax_rate / 100
sales_tax = sales_tax_rate_percent * subtotal
print(f"Sales Tax: ${sales_tax:.2f}") 

total_amount = subtotal + sales_tax
print(f"Total: ${total_amount:.2f}")

print()

payment_amount = float(input("What is the payment amount? "))
change = payment_amount  - total_amount
print(f"Change: ${change:.2f}")