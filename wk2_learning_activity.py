# user_age = input("How old are you? ")
# new_age = int(user_age) + 1

# print(f"On your next birthday, you will be {new_age}")

# egg_cartons = input("How many egg cartons do you have? ")
# total_eggs = int(egg_cartons) * 12

# print (f"You have {total_eggs} eggs.")

# total_cookies = input("How many cookies do you have? ")
# total_people = input("How many people are there? ")

# cookie_per_person = int(total_cookies) / int(total_people)

# print(f"Each person may have {cookie_per_person} cookies.")



# fahrenheit_temp = input("Whai is your temp in Fahrenheit? ")
# celsius_temp = (float(fahrenheit_temp) - 32) * (5/9)

# print(f"The temperature in Celsius is {celsius_temp:.1f} degrees.")







import math

square_length = input("What is the length of a side of the square? ")
square_area = float(square_length) ** 2
print(f"The area of the square is: {square_area}")

rectangle_lenth = input("What is the length of the rectangle? ")
rectangle_width = input("What is the width of the rectangle? ")
rectangle_area = float(rectangle_lenth) * float(rectangle_width)
print(f"The area of the rectangle is: {rectangle_area}")


circle_radius = input("What is the radius of the circle? ")
circle_area = math.pi * (float(circle_radius) ** 2)
print(f"The area of the circle is: {circle_area:.2f}")