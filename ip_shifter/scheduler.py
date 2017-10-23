''' IP scheduler '''

# import os
# import sys
# import shutil
# import random
# import pyperclip

# Import utility functions
UTILITIES = __import__('util')


def start(nic):
    ''' Starting the IP shifting... '''

    config = UTILITIES.get_config()
    ip_list = UTILITIES.prepare_ip_range(config['start'], config['end'])

    print(nic, ip_list)

    # TODO step 1: change IP address
    # TODO step 2: wait 5 secs
    # TODO step 3: check connection, return to step 1 if not working


def ip_shifter(nic, ip_address, gateway):
    ''' Initialize ip shifting mechanism on provided NIC '''

    # IP address, subnetmask and gateway values should be unicode objects
    ip_address = ip_address.encode("utf-8")
    gateway = gateway.encode('utf-8')
    subnetmask = u'255.255.0.0'

    # Set IP address, subnetmask and default gateway
    # Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
    nic.EnableStatic(IPAddress=[ip_address], SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway])
