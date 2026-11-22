number = 0

# Keep looping as long as the number is less than 10
while number < 10:
    number = int(input("What is the number? "))

print("Finished with the loop")


# Start with the number 1
number = int(input("Enter a number: "))

# Keep looping as long as the number is less than or equal to 5
while number <= 5:
    # Display the number
    print(f"The number is: {number}")

    # Update the number to be one more than it was
    number = number + 1 

print("Finished with the loop")



number = -1

while number < 0:
    number = int(input("Please type in a positive number: "))

    print("Sorry, that is a negative number. Please try again.")

print(f"The number is: {number}")


reply = "no"

while reply == "no":
    reply = input("May I have a piece of candy? ").lower()


if reply == "yes":
    print ("Thank you.")

else:
print("wrong input")





colors = ["red", "blue", "green", "yellow"]
for i in colors:
    print(i)

for j in range(9):
    print (j)

for k in range(2,21,2):
    print(k)



word = "book"
number_of_letters = 4

for index in range(len(word)):
    letter = word[index]
    print(letter)





user_favourite_letter = input("What is your favourite letter? ").lower()
programmed_word = "Commitment"

for letter in programmed_word:
    if letter == user_favourite_letter:
        print("_", end="")
    else:
        print (letter, end="")



import random

def generate_feedback(secret, guess):
    # Normalize to lowercase for comparison
    secret = secret.lower()
    guess = guess.lower()

    # First pass: mark correct positions
    feedback = ['_'] * 6
    secret_marks = [False] * 6  # which letters in secret have been matched
    guess_marks = [False] * 6   # which positions in guess have been matched

    # Mark exact matches with uppercase in the final feedback
    for i in range(6):
        if guess[i] == secret[i]:
            feedback[i] = secret[i].upper()
            secret_marks[i] = True
            guess_marks[i] = True

    # Second pass: mark present letters in wrong positions
    for i in range(6):
        if not guess_marks[i]:
            for j in range(6):
                if not secret_marks[j] and guess[i] == secret[j]:
                    # mark as lowercase since it's present but misplaced
                    feedback[i] = guess[i]
                    secret_marks[j] = True
                    guess_marks[i] = True
                    break

    return feedback

def is_valid_guess(guess):
    return len(guess) == 6 and guess.isalpha()

def play_word_guess(secret_word=None, max_guesses=6):
    # Optional: set a fixed secret word for testing
    if secret_word is None:
        # You can replace this with a random choice from a list of 6-letter words
        word_list = [
            "mosiah", "moroni", "temple", "agency", "galaxy",
            "planet", "oracle", "bridge", "sphinx", "athena"
        ]
        secret_word = random.choice(word_list).lower()

    print("Welcome to the word guessing game!")
    print("Hint format: each position shows _ (unknown), a letter in uppercase if correct position, or lowercase if present elsewhere.")
    # You may display no hint at start to match the log style
    # print("_ _ _ _ _ _")

    guesses = 0
    while guesses < max_guesses:
        user = input("Your guess (6 letters): ").strip()
        if not is_valid_guess(user):
            print("Please enter exactly 6 alphabetic characters.")
            continue

        guesses += 1
        feedback = generate_feedback(secret_word, user)
        # Display feedback with spaces between for readability
        print("Hint:", " ".join(feedback))

        if user.lower() == secret_word:
            print(f"Congratulations! You guessed it! It took you {guesses} guesses.")
            return

        # Optional: reveal if they want after each guess
        print()

    print(f"Sorry, you've used all {max_guesses} guesses. The word was: {secret_word.upper()}")

if __name__ == "__main__":
    # To test, you can fix the secret word, e.g.:
    # play_word_guess(secret_word="mosiah")
    play_word_guess()