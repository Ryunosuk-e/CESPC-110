#for Additional creativity, i noticed that when the player makes a guess and none of the letters are present in thr secret word, no hint is returned. so i made it in a way that the program still returns a hint so player can know current status instead of just asked to try again. kept running into errors, so i had to restructure the whole thing, or some rather.
print()
print("Welcome to the word guessing game! ")
print()

secret_word = "great"
guesses = 0
user_guess = ""

hint = ["_" for letter in secret_word] 
print("Your hint is:", " ".join(hint))
        
done = False
while not done and user_guess != secret_word:

    user_guess = input("What is your guess? ").lower()

    if user_guess == "end":
        print("Game terminated by user.")
        done = True
        continue

    if len(user_guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue

    guesses = guesses + 1

    if user_guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {guesses} guesses.")
    else:
        hint = ["_"] * len(secret_word)
        secret_remaining = list(secret_word)

    
        for i in range(len(secret_word)):
            if user_guess[i] == secret_word[i]:
                hint[i] = secret_word[i].upper()
                secret_remaining[i] = None

        
        for i in range(len(secret_word)):
            if hint[i] == "_":
                if user_guess[i] in secret_remaining:
                    hint[i] = user_guess[i].lower()
                    
                    secret_remaining[secret_remaining.index(user_guess[i])] = None

        print("Your hint is:", " ".join(hint))

print("Thanks for playing.")
print("Do come back again.")
