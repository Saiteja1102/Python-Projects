import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
for i in chosen_word:
    print("_",end="")
print()
word_len = len(chosen_word)
correct_letters = []
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
        lives -= 1
    print(word)
    print(stages[lives])
    if lives == 0:
        print("Game Over")
        break