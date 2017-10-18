name = 10

print('Only minion can pass this test! (-.- )')

while name != 'minion':
    name = input()

print('Go Again!')

while True:
    name = input()
    if name == 'minion':
        break

print('Hah!')
