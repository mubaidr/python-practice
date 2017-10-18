# This progam generates collatz sequence

print('This progam generates collatz sequence. \n\n')


def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = (number * 3) + 1
    print(result)
    return result


print('Go ahead and type any number: ')

while True:
    try:
        global NUMBER
        NUMBER = int(input())
        break
    except ValueError:
        print('Invalid input, try again: ')

RES = NUMBER
while RES != 1:
    RES = collatz(RES)

print('\n\nFinished!')

exit()
