""" IP Changer Module """

import os
import sys
import shutil
import random
import pyperclip

# Welcome message
print('\nHello!\n')
print('   ;')
print('  /_\\')
print('\\(o.o)')
print('  ) (\\')
print('  / \\\n\n')

# Import utility functions
UTILITIES = __import__('util')
# Collect system NICs
NIC_CONFIGS = UTILITIES.get_nic_list()
# Get target NIC from user
SELECTED_NIC = UTILITIES.get_nic_input(NIC_CONFIGS)
