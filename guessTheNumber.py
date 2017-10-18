import random

retries = 0
number = random.randint(0, 10)
guessInput = None

print('Guess the number')
print('Guess: ')

while True:
    retries = retries + 1
    try:
        guessInput = int(input())

        if guessInput != number:
            print('Invalid guess, please try again!')
        else:
            msg = 'You have successfuly guessed the number in {r} retries! |( -.-)/'.format(
                r=retries)
            print(msg)
            break
    except:
        print('Invalid input! Please enter a valid number.')
        print('Guess: ')

exit()
