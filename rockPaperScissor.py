import random
import time
import sys

print('''Rock, Paper, Scissors
      - Rock beats Scissors.
      - Paper beats Rocks.
      - Scissors beats Paper.''')

Wins = 0
Losses = 0
Ties = 0

while True:
    while True:
        print('{} Wins, {} Losses, {} Ties'.format(Wins, Losses, Ties))
        playerMove = input('Enter your move: (R)ock, (P)aper, (S)cissor or (Q)uit > ').upper()
        
        if playerMove == 'Q':
               print("Thank you for playing")
               sys.exit()
     
        # Display what the player chose:
        if playerMove == "R":
              print('ROCK versus...')
              playerMove = 'ROCK'
        elif playerMove == "P":
                print('PAPER versus...')
                playerMove = 'PAPER'
        elif playerMove == "S":
                print('SCISSOR versus...')
                playerMove = 'SCISSOR'
        else:
            print("Type one of R, P, S, OR Q")
            break
        
        # Count to three with dramatic pauses:
        time.sleep(0.5)
        print('1...')
        time.sleep(0.25)
        print('2...')
        time.sleep(0.25)
        print('3...')
        time.sleep(0.25)
        
        # Display what the computer chose:
        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            computerMove = 'ROCK'
        elif randomNumber == 2:
            computerMove = 'PAPER'
        elif randomNumber == 3:
            computerMove = 'SCISSOR'
        print("hit> ", computerMove)
        time.sleep(0.5)
        
        # Display and record the win/loss/tie:
        if playerMove == computerMove:
            print('it\'s a tie!')
            Ties = Ties + 1
        elif playerMove == 'ROCK' and computerMove == 'SCISSOR':
            print('You win!')
            Wins = Wins + 1
        elif playerMove == 'PAPER' and computerMove == 'ROCK':
            print('You win!')
            Wins = Wins + 1
        elif playerMove == 'SCISSOR' and computerMove == 'PAPER':
            print('You win!')
            Wins = Wins + 1
        elif playerMove == 'ROCK' and computerMove == 'PAPER':
            print('You lose!')
            Losses = Losses + 1
        elif playerMove == 'PAPER' and computerMove == 'SCISSOR':
            print('You lose!')
            Losses = Losses + 1
        elif playerMove == 'SCISSOR' and computerMove == 'ROCK':
            print('You lose!')
            Losses = Losses + 1
