""" IP Changer Module """

import os
import sys
import shutil
import random
import pyperclip

# Import utility functions
UTILITIES = __import__('util')

# Welcome message
print('\nHello!\n')
print('   ;')
print('  /_\\')
print('\\(o.o)')
print('  ) (\\')
print('  / \\\n\n')

# Collect system NICs
SELECTED_NIC = None
NIC_CONFIGS = UTILITIES.get_nic_list()
UTILITIES.print_nic_list(NIC_CONFIGS)

# Get target NIC from user
print('\nPlease select an NIC adapter: \n')
while SELECTED_NIC is None or SELECTED_NIC < 0 or SELECTED_NIC > len(NIC_CONFIGS):
    try:
        SELECTED_NIC = int(input()) - 1
    except ValueError:
        print('Invalid input, please try again: ')
        SELECTED_NIC = None
UTILITIES.print_nic_name(NIC_CONFIGS[SELECTED_NIC])
