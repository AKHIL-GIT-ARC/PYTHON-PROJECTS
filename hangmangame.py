#HANGMAN GAME 

import random,time
from words import *

dictionary_art = {0 : ("      ",
                       "      ",
                       "      "),
                  1 : ("  𐩒   ",
                       "      ",
                       "      "),
                  2 : ("  𐩒   ",
                       "  |   ",
                       "      "),
                  3 : ("  𐩒   ",
                       " /|   ",
                       "      "),
                  4 : ("  𐩒   ",
                       " /|\\ ",
                       "      "),
                  5 : ("  𐩒    ",
                       " /|\\  ",
                       " /     "),
                  6 : ("  𐩒    ",
                       " /|\\  ",
                       " / \\  ")}


def display_art(wrong_guesses):
    print("-----HANGMAN-----")
    for line in dictionary_art[wrong_guesses]:
        print(f"     {line}     ")

    print("-----------------")

def display_hint(hint):
    print("HINT:")
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"]*len(answer)
    guessed_letters = set()
    wrong_guesses = 0
    is_running = True

    while is_running:
        print("---$$$ WELCOME TO AKHIL'S HANGMAN GAME $$$---")
        display_art(wrong_guesses)
        display_hint(hint)
        guess = input("Enter your guess(letter):").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("-----INVALID INPUT-----\n!ENTER ONLY ONE LETTER!")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already been guessed.")
            continue
        
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] =  guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_art(wrong_guesses)
            display_answer(answer)
            print("CONGRATULATIONS..YOU HAVE GUESSED THE WORD")
            print(f"You took {len(guessed_letters)} attempts to guess the word..")
            is_running = False 
        elif wrong_guesses >= len(dictionary_art) - 1:
            display_art(wrong_guesses)
            display_answer(answer)
            print("OOPS...YOU FAILED IN GUESSING THE WORD \n-BETTER LUCK NEXT TIME.......") 
            is_running = False
        
    play_again = input("Do you want to play again (y/n):").upper()
    if play_again == 'Y':
        print("LOADING THE GAME AGAIN....")
        time.sleep(3)
        main()
    else:
        print("THANKS FOR PLAYING OUR HANGMAN GAME 😊")

if __name__ == '__main__':
    main()