print()
print("Welcome to the word guessing game! ")
print()

secret_word = "great"
guesses = 0
user_guess = ""

hint = ["_"for letter in secret_word] 
print("Your hint is:", " ".join(hint))
        
done = False
while not done and user_guess != secret_word:

    user_guess = input("What is your guess? ").lower()
    guesses = guesses + 1 

    if user_guess == "end":
        print("Game terminated by user.")
        done = True
        continue

    if len(user_guess) == len(secret_word):

        if user_guess != secret_word:
            secret_remaining = list(secret_word)


            for i in range(len(secret_word)):
                if user_guess[i] == secret_word[i]:
                    hint[i] = secret_word[i].upper()
                    

           
            for i in range(len(secret_word)):
                if hint[i] != '_':
                    continue  

                if user_guess[i] in secret_remaining:
                    hint[i] = user_guess[i].lower()
        
                    print("Your hint is:", " ".join(hint))
        else:
            print("Congratulations! You guessed it!")
            print(f"It took you {guesses} guesses.")

    else:
        print("Sorry, the guess must have the same number of letters as the secret word.")

    
print("Thanks for playing.")
print("Do come back again.")