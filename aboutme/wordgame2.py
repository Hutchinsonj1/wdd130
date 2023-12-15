"""
File: wordgame2.py
Author: Jaden Hutchinson

Purpose: Make a word game
"""
secret = "mosiah"
guess = ""
count = 0

#initial hint:
hint = "Your hint is: "
for a in secret:
    hint = hint + "_ "
print(hint)

while guess != secret:
    # My first attempt below, but needed it to Loop
  # while len(guess) != len(secret):
    #    print("Sorry, the guess must have the same number of letters as the secret word.")

    same_length = False
    while(not same_length):
        guess = input("What is your guess? ").lower()
        count += 1

        if len(guess) != len(secret):
            print("Sorry, the guess must have the same number of letters as the secret word.")
        else:
            same_length = True

    if guess == secret:
        break

    letter = "_ "
    hint = ""

    for i, a in enumerate(guess):
        letter = "_ "
        for j, b in enumerate(secret):
            if a == b and i == j:
                letter = a.capitalize() + " "
            elif a == b:
                letter = a + " "

        hint = hint + letter
    print(f"Your hint is: {hint}")

if count < 2:
    print(f"You guessed correctly in {count} guess! You are a winner!")
else:
    print(f"You guessed correctly in {count} guesses!!")



