''' IP scheduler '''

import signal
import sys
import time

# Import utility functions
UTILITIES = __import__('util')


def start(nic_index):
    ''' Starting the IP shifting... '''

    config = UTILITIES.get_config()
    ip_list = UTILITIES.prepare_ip_range(
        config['ip']['start'], config['ip']['end'])

    for ip_address in ip_list:
        set_ip_address(nic_index, ip_address, config)
        print('IP Address: {}\n'.format(ip_address))
        time.sleep(config['timeout'])
        if UTILITIES.is_connected():
            print('Connection seems good, waiting... \n')
            time.sleep(config['delay'])


def set_ip_address(nic_index, ip_address, cfg):
    ''' Initialize ip shifting mechanism on provided NIC '''

    nics = UTILITIES.get_nic_list()
    nic = nics[nic_index]

    try:
        nic.EnableStatic(IPAddress=[ip_address],
                         SubnetMask=[cfg['subnet']])
        nic.SetGateways(DefaultIPGateway=[cfg['gateway']])
    except:
        print('Doh... Some unexpected error occured!')
        exit()
