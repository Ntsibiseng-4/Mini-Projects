import random
import string

print("WELCOME TO PASSWORD PICKER")

ADJECTIVES = ['sleepy', 'slow', 'smelly',
 'wet', 'fat', 'red',
 'orange', 'yellow', 'green',
 'blue', 'purple', 'fluffy',
 'white', 'proud', 'brave']

NOUNS = ['apple', 'dinosaur', 'ball',
 'toaster', 'goat', 'dragon',
 'hammer', 'duck', 'panda']


# for num in range(3): #The for loop runs 3 times, and selects 3 different passwords
while True:
    adjective = random.choice(ADJECTIVES)
    noun = random.choice(NOUNS)
    character = random.choice(string.punctuation)
    number = random.randrange(0, 100)
    
    PASSWORD = adjective + noun + character + str(number)
    print(f'Your password is {PASSWORD}')
    
    respond = input("Would you like another password? Type y or n ")
    if respond == "n":
      break