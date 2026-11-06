SCORE = 0

def multiple_Choice(guess, answer):
    global SCORE
    ATTEMPTS = 0
    guessing = True
    
    while guessing and ATTEMPTS < 3:
        if guess.upper() == answer.upper(): 
          print(f'{answer} ✅Correct')
          SCORE += 5 - ATTEMPTS
          guessing = False
        else:
            if ATTEMPTS < 3:
                guess = input("Sorry wrong answer, try again! ")
                ATTEMPTS += 1
                SCORE += 3 - ATTEMPTS
                
    if guessing:
        print(f'❌Incorrect, the answer is {answer} ')
        SCORE += 1 - ATTEMPTS
        
    return SCORE

print("MULTIPLE CHOICE")
guess1 = input("Who built the ark?\n A) Moses\n B) Noah\n C) Abraham\n D) David\n > ")
multiple_Choice(guess1, 'B')
guess2 = input("How many days did God take to create the world?\n A) 5\n B) 7\n C) 6\n D) 10\n > ")
multiple_Choice(guess2, 'C')
guess3 = input("Which book is the first in the Bible?\n A) Exodus\n B) Psalms\n C) Genesis\n D) Matthew\n > ")
multiple_Choice(guess3, 'C')


def oneAnswer(guess1, answer1):
    global SCORE
    ATTEMPTS = 0
    
    guess_bool = guess1.lower() == "true"  #returns a boolean  
    
    if guess_bool == answer1:
        print("✅ Correct")
        SCORE += 2 - ATTEMPTS
    else:
        print("❌ Incorrect")
        SCORE += 1
    return SCORE

print("\n")
print("TRUE or FALSE QUESTIONS")
guess4 = input("Jesus was born in Bethlehem\n > ")
oneAnswer(guess4, True)
guess5 = input("Johan was swallowed by a lion\n > ")
oneAnswer(guess5, False)
guess6 = input("Samson's strength was in his hair\n > ")
oneAnswer(guess6, True)

print(f"Final score: {SCORE}")