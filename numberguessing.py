#python number guessing game
import random

low = 1
high = 10
answer = random.randint(low, high)
guesses = 0
is_running = True

print("----Welcome to number guessing game----")
print(f"Select a number between {low} and {high}")

while is_running:
    guess_str = input("Enter your guess: ").strip()
    if not guess_str or not guess_str.isdigit():
        print("Invalid input. Please enter a number between {low} and {high}.")
        continue
    
    guess = int(guess_str)
    guesses += 1
    
    if guess < low or guess > high:
        print("Number out of range.")
        print(f"Please enter a number between {low} and {high}")
        continue
    elif guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print("Correct! You made it.")
        print(f"Number of guesses: {guesses}")
        is_running = False
