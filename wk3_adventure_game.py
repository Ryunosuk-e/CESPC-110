#For additional creativity, I used the while loop. This will enable the player to try again when an invalid answer is entered.
try_again = "yes"

while try_again != "no":
    user_input_level_1 = input("You're walking through a Dark ruined Village, and find two items a LANTERN and a KEY. Which one do you want to pick up? ").lower()

    if user_input_level_1 == "lantern":
        user_input_level_2a = input("You’ve lit the lantern, the path before you is illuminated. You catch the attention of a wild boar. do you want to RUN or Turn OFF the lantern? ").lower()

        if user_input_level_2a == "run":
            user_input_level_3a = input("You run off into the nearby woods, in your haste, you drop your lantern, do you want to stop and PICK it up, LEAVE it and continue running or STAND your ground and confront the Boar? ").lower()

            if user_input_level_3a == "pick":
                print("success")
            elif user_input_level_3a == "leave":
                print("success")
            elif user_input_level_3a == "stand":
                print("success")
            else:
                try_again = input("Wrong Entry, Would you like to try again? (You will start from the very beginning.)" ).lower()

        elif user_input_level_2a == "off":
            user_input_level_3b = input("you've snuffed the Lantern, you move in pure darkness. With the help of the moon, you come across a small cabin. Do you want to have a look INSIDE or SEARCH around for a weapon to defend yourself? ").lower()

            if user_input_level_3b == "inside":
                print("success")
            elif user_input_level_3b == "search":
                print("success")
            else:
                try_again = input("Wrong Entry, Would you like to try again? (You will start from the very beginning.)" ).lower()

        else:
            try_again = input("Wrong Entry, Would you like to try again? (You will start from the very beginning.)").lower()

    elif user_input_level_1 == "key":
        user_input_level_2b = input("You've picked up a key. The key fits a sealed door at the outskirts. On your way there, you trip on a log and fall, you hear rustling coming from a small bush nearby. Do you want to stay on the FLOOR or STAND and continue to the door? ").lower()

        if user_input_level_2b == "floor":
            user_input_level_3c = input("You stay down to listen as rustling grows closer.A hedgehog-like creature came out from the underbrush and sniffs the air, then runs off. Do you want to CHASE after it or STAY there a while? ").lower()

            if user_input_level_3c == "chase":
                print("success")
            elif user_input_level_3c == "stay":
                print("success")
            else:
                try_again = input("Wrong Entry, Would you like to try again? (You will start from the very beginning.) ").lower()

        elif user_input_level_2b == "stand":
            user_input_level_3d = input("You stand and brush dirt from your knee, and continues towards the door. Do you want to OPEN the door or GO through the back? ").lower()

            if user_input_level_3d == "open":
                print("success")
            elif user_input_level_3d == "go":
                print("success")
            else:
                try_again = input("Wrong Entry, Would you like to try again? (You will start from the very beginning.) ").lower()

        else:
            try_again = input("Wrong Entry, Would you like to try again? (You will start from the very beginning.) ").lower()

    else: 
        try_again = input("Wrong Entry, Would you like to try again? ").lower()

print("Thank you for playing")