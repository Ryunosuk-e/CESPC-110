import random

random_number = random.randint(1, 100)
print(random_number)
guesses = 0

user_guess = ""
play_again = "yes"

while play_again != "no":
    while user_guess != random_number:

        user_guess = int(input("What is your guess? "))
        guesses = guesses + 1

        if user_guess < random_number:
            print("Higher")
        elif user_guess > random_number:
            print("Lower")
        else:
            user_guess == random_number
            print("You guessed it!")
            print(f"It took you {guesses} guesses")

    play_again = input("Would you like to play again (yes/no)? ").lower() .strip()
    if play_again != "yes":
        print("Thank you for playing. Goodbye.")
        break







# import random

# def play_round():
#     secret = random.randint(1, 100)
#     guesses = 0

#     while True:
#         try:
#             guess = int(input("What is your guess? "))
#         except ValueError:
#             print("Please enter an integer.")
#             continue

#         guesses += 1

#         if guess < secret:
#             print("Higher")
#         elif guess > secret:
#             print("Lower")
#         else:
#             print("You guessed it!")
#             print(f"It took you {guesses} guesses")
#             break

# def main():
#     print("Welcome to the Guess the Number game!")
#     while True:
#         play_round()
#         again = input("Would you like to play again (yes/no)? ").strip().lower()
#         if again != "yes":
#             print("Thank you for playing. Goodbye.")
#             break

# if __name__ == "__main__":
#     main()