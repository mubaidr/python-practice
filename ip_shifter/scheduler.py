''' IP scheduler '''

import time

# Import utility functions
UTILITIES = __import__('util')


def start(nic):
    ''' Starting the IP shifting... '''

    config = UTILITIES.get_config()
    ip_list = UTILITIES.prepare_ip_range(config['start'], config['end'])

    for ip_address in ip_list:
        set_ip_address(nic, ip_address, config['gateway'])
        print('IP Address: {}\n'.format(ip_address))
        time.sleep(config['timeout'])
        if UTILITIES.is_connected():
            print('Connection seems good, waiting... \n')
            time.sleep(config['delay'])


def set_ip_address(nic, ip_address, gateway):
    ''' Initialize ip shifting mechanism on provided NIC '''

    # IP address, subnetmask and gateway values should be unicode objects
    #ip_address = ip_address.encode("utf-8")
    ip_address = u'111.111.111.111'
    gateway = u'111.111.111.100'
    subnetmask = u'255.255.0.0'
    #gateway = u'192.168.168.192'
# Set IP address, subnetmask and default gateway
# Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
    try:
        nic.EnableStatic(IPAddress=[ip_address], SubnetMask=[subnetmask])
        nic.SetGateways(DefaultIPGateway=[gateway])
    except:
        print('Doh...')
