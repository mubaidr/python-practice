#! python3
# # pw.py - An insecure password locker program.

import sys
import pyperclip

if len(sys.argv) < 2:
    print(
        'Missing account name. Usage: python pw.py [account] - copy account password')
    sys.exit()
else:
    global ACCOUNT
    ACCOUNT = sys.argv[1]

PASSWORDS = {
    'gmail': 'Ullamco incididunt veniam',
    'twitter': 'Enim incididunt',
    'npm': 'Quis est culpa'
}

if ACCOUNT in PASSWORDS.keys():
    # copy to clipboard
    PASSWORD = PASSWORDS.get(ACCOUNT)
    pyperclip.copy(PASSWORD)
    print('Password is copied to clipboard. \\(-_-)')
else:
    print('Account not found!')
