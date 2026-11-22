user_input_level_1 = input("You're walking through a Dark ruined Village, and find two items a LANTERN and a KEY. Which one do you want to pick up? ").lower()

if user_input_level_1 == "lantern":
    user_input_level_2a = input("You’ve lit the lantern, the path before you is illuminated. You catch the attention of a wild boar. do you want to RUN or Turn OFF the lantern? ").lower()

    if user_input_level_2a == "pick":
        print("success")
    elif user_input_level_2a == "leave":
        print("success")
    else:
        print("Wrong Entry, Please start again")

elif user_input_level_1 == "key":
    user_input_level_2b = input("There is a The key fits a sealed door at the outskirts. On your way there, you trip on a log and fall, you hear rustling coming from a small bush nearby. Do you want to stay on the FLOOR or STAND and continue to the door? ").lower()

    if user_input_level_2b == "pick":
        print("success")
    elif user_input_level_2b == "leave":
        print("success")
    else:
        print("Wrong Entry, Please start again")

else: 
    print("Wrong Entry, Please start again")