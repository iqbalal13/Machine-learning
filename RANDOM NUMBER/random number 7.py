import random

print("Welcome to the Number Guessing Game!")
print("You have to guess a number between 1 to 10.")

MAX_GUESSES = 10
num_guesses = 0

while num_guesses < MAX_GUESSES:
    player_guess = int(input("Enter your guess: "))
    computer_guess = random.randint(1, 10)

    if player_guess == computer_guess:
        print("Congratulations! You win!")
        break
    else:
        print("Oops! Computer wins.")
        num_guesses += 1

if num_guesses == MAX_GUESSES:
    print("Sorry, you didn't guess the number in time. Game over.")

print("Thank you for playing!")