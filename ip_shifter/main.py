''' IP Changer Module '''

import signal
from win32com.shell import shell
# Import scheduler functions
SCHEDULER = __import__('scheduler')
# Import utility functions
UTILITIES = __import__('util')

signal.signal(signal.SIGINT, UTILITIES.signal_handler)

if shell.IsUserAnAdmin() != True:
    print('\nI hate non-admin users! (-_- )\n')
    exit()
else:
    # Welcome message
    print('\nHello!\n')
    print('   ;')
    print('  /_\\')
    print('\\(o.o)')
    print('  ) (\\')
    print('  / \\\n\n')

    # Collect system NICs
    NIC_CONFIGS = UTILITIES.get_nic_list()
    # Print system NICs
    UTILITIES.print_nic_list(NIC_CONFIGS)
    # Get target NIC from user
    SELECTED_NIC = UTILITIES.get_nic_input(NIC_CONFIGS)
    # start the process
    SCHEDULER.start(SELECTED_NIC)
