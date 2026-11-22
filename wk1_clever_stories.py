# Note additions on lines 6,12,15,23 & 24. I have added a variable that will request the users first name and another adjective. I also printed the requested first name in addition to output on line 16 and added two lines to the story.

print("Please enter the following:")
print()

first_name = input("first name: ")
adjective = input("adjective: ")
animal = input("animal: ")
verb_1 = input("verb: ")
exclamation = input("exclamation: ")
verb_2 = input("verb: ")
verb_3 = input("verb: ")
adjective_2 = input("adjective: ")
print()

print(f"Hi {first_name.capitalize()}, Your story is:")
print()

print(f"The other day, I was really in trouble. It all started when I saw a very")
print(f'{adjective} {animal} {verb_1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all')
print(f"I could think to do was to {verb_2} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb_3}")
print("right in front of my family.")
print(f"I lowered my voice, surprised by how {adjective_2} the {animal} made me feel.")
print(f"The {animal} introduced itself as Terran.")



