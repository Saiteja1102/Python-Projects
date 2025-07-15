import random

from hangman_words import word_list
from hangman_art import logo, stages

print(logo)
lives = 6
print("-------------------------------------------")
print("Guess The Telugu Movie Hangman Version!!" )
chosen_word = random.choice(word_list)
for i in chosen_word:
    print("_",end="")
print()
word_len = len(chosen_word)
correct_letters = []
already_guessed = []
word = ""
while word != chosen_word:
    guess = input("Guess a letter? ").lower()
    word = ""
    for letter in chosen_word:
        if guess == letter:
            word = word + guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            word = word + letter
        else:
            word = word + "_"
    if guess not in correct_letters:
        if guess in already_guessed:
            print(f"You have already guessed {guess}")
        else:
            already_guessed.append(guess)
            lives -= 1
    print(word)
    print(stages[lives])
    if lives == 0:
        print("Game Over")
        print(f"Ans is: {chosen_word}")
        break

if word == chosen_word:
    print(f"You have {lives} lives remaining")
    print("You Win")
print("-----------------------------------------------")