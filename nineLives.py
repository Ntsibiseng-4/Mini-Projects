import random

lives = 9
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane']
secret_word = random.choice(words)
clues = ['?', '?', '?', '?', '?']
heart_symbol = u'\u2764'
guessed_word_corectly = False

# The function insert the correct letter at its position, using the index
def update_clue(guessed_letter, secret_word, clues):
    index = 0
    while index < len(secret_word):
       if  guessed_letter == secret_word[index]:
           clues[index] = guessed_letter
       index += 1

while lives > 0:
    print(clues)
    print("Lives left: " + heart_symbol * lives)
    guess = input("Guess a letter or the whole word: ")
    
    if guess == secret_word:
        guessed_word_corectly = True
        break
    
    if guess in secret_word:
        update_clue(guess, secret_word, clues) 
        if '?' not in clues:
            guessed_word_corectly = True
    else:
        print("Incorrect. You lose a life")    
        lives -= 1
        
if guessed_word_corectly:
    print(f"You won! The secret word was {secret_word}")   
else:
    print(f"You lost! The secret word was {secret_word}") 