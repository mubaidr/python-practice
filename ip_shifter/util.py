''' Utility functions '''

import socket
import re
import wmi
# import pypiwin32


def get_nic_input(configs):
    ''' Get NIC input from user and prints the name of the same'''
    selected_nic = None
    print('\nPlease select an NIC adapter: \n')
    while selected_nic is None:
        try:
            selected_nic = int(input()) - 1
        except ValueError:
            print(
                'Invalid input, please enter an integer between 1-{0}'.format(len(configs)))
            selected_nic = None
        if selected_nic < 0 or selected_nic > len(configs):
            print(
                'Invalid input, please enter an integer between 1-{0}'.format(len(configs)))
            selected_nic = None

    print_nic_name(configs[selected_nic])
    return selected_nic


def simplify_nic_name(cfg):
    ''' Removes numbering from NIC names'''
    regex = re.compile(r'\[[0-9]{8}\]', re.IGNORECASE)
    return re.sub(regex, '', cfg.Caption)


def print_nic_list(configs):
    ''' Prints NIC names from the config list '''
    for index, config in enumerate(configs):
        name = simplify_nic_name(config)
        print('{0}: {1}'.format(index + 1, name))


def print_nic_name(config):
    ''' Prints NIC name from the config '''
    print('\nTarget NIC: {0}\n'.format(simplify_nic_name(config)))


def get_nic_name(config):
    ''' Returns NIC name from the config '''
    return simplify_nic_name(config)


def get_nic_list():
    ''' Obtain network adaptors configurations '''
    configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    print_nic_list(configs)
    return configs


def is_connected():
    ''' Check if internet connection is working '''
    remote_server = "www.google.com"
    try:
        host = socket.gethostbyname(remote_server)
        socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False
