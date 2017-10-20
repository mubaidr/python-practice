''' IP scheduler '''

import os
import sys
import shutil
import random
import pyperclip

# Import utility functions
UTILITIES = __import__('util')


def start():
    ''' Starting the IP shifting... '''

    CONFIG = UTILITIES.get_config()

    print(CONFIG)

    # TODO get config.txt
    # TODO prepare range of ip address list
    # TODO step 1: change IP address
    # TODO step 2: wait 5 secs
    # TODO step 3: check connection, return to step 1 if not working


def ip_shifter(nic):
    ''' Initialize ip shifting mechanism on provided NIC '''

    # IP address, subnetmask and gateway values should be unicode objects
    ip_address = u'192.168.0.11'
    subnetmask = u'255.255.255.0'
    gateway = u'192.168.0.1'

    # Set IP address, subnetmask and default gateway
    # Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
    nic.EnableStatic(IPAddress=[ip_address], SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway])
