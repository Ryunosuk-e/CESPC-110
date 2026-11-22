# open ("courses.txt")

# with open("courses.txt") as courses_file:
#     for line in courses_file:
#         print(line)


# with open("books.txt") as books_file:
#     for book in books_file:
#         book_list = book.strip()
#         print (book_list)


people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngest_name = ""
youngest_age = 50

# for person in people:
#     print(person)

for person in people:
    name , age = person.split(" ") 
    age = int(age)
    print(name, age)


    if age < youngest_age:
        youngest_age = age
        youngest_name = name

print(f"Youngest person: {youngest_name}, {youngest_age}")
   


