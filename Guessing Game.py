# Guessing Game

right_guess = 9
chances = 0
count =0
#number = int(input('Guess: '))

# your_chance = len(number)

while chances < 3:
    number = int(input('Guess: '))
    chances += 1

    if right_guess == number:
        print('You guessed right')
        break
    else:
        print('Wrong, Try again')

