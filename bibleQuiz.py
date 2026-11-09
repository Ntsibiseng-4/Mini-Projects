def guess_check(guess, answer):
    global score
    attempt = 0
    still_guess = True
    
    while still_guess and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct answer.")
            score += 1
            still_guess = False
        else:
            if attempt < 3:
              guess = input("Sorry wrong answer. Try again! ")
              attempt += 1
        
    if still_guess:
        print("The correct answer is: " + answer)
        
            

score = 0
print("Guess the character.")
guess1 = input("I was a shepherd boy, became king, and wrote many Psalms. I defeated a giant with one stone. Who am I? ")
guess_check(guess1, 'David')
guess2 = input("I was sold by my brothers into slavery in Egypt, interpreted dreams of Pharaoh, and became second-in-command of Egypt. Who am I? ")
guess_check(guess2, 'Joseph')
guess3 = input("I was a firsherman, called Rock, and I denied Jesus 3 times before the rooster crowed. Who am I? ")
guess_check(guess3, 'Peter')
guess4 = input("I was the mother of Jesus. Who am I? ")
guess_check(guess4, 'Mary')
guess5 = input("I was swallowed by a fish after running away from God's call to Nineveh. Who am I? ")
guess_check(guess5, 'Jonah')
print("You scored: ", score)

if  score == 5:
    print("Well  done, you got them all.")
elif score == 3 or score == 4:
    print("Well done.")
elif score < 1:
    print("Try reading the Bible more")
else:
    print("Improve your Bible reading")
            