print()
print("Welcome to the word guessing game! ")
print()

secret_word = "great"
guesses = 0
user_guess = ""

while user_guess != secret_word:

    user_guess = input("What is your guess? ").lower()
    guesses = guesses + 1 

    if user_guess != secret_word:
        print("Your guess was not correct.")
    else:
        print("Congratulations! You guessed it!")
        print(f"It took you {guesses} guesses.")