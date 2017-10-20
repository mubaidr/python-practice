''' Utility functions '''

import socket
import re
import wmi
# import pypiwin32


def simpleify_nic_name(cfg):
    ''' Removes numbering from NIC names'''
    regex = re.compile(r'\[[0-9]{8}\]', re.IGNORECASE)
    return re.sub(regex, '', cfg.Caption)


def print_nic_list(configs):
    ''' Prints NIC names from the config list '''
    for index, config in enumerate(configs):
        name = simpleify_nic_name(config)
        print('{0}: {1}'.format(index + 1, name))


def print_nic_name(config):
    ''' Prints NIC name from the config '''
    print('\nTarget NIC: {0}\n'.format(simpleify_nic_name(config)))


def get_nic_name(config):
    ''' Returns NIC name from the config '''
    return simpleify_nic_name(config)


def get_nic_list():
    ''' Obtain network adaptors configurations '''
    configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    return configs


def ip_shifter(nic):
    ''' Initilize ipshifting mechanism on provided NIC '''

    # IP address, subnetmask and gateway values should be unicode objects
    ip_address = u'192.168.0.11'
    subnetmask = u'255.255.255.0'
    gateway = u'192.168.0.1'

    # Set IP address, subnetmask and default gateway
    # Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
    nic.EnableStatic(IPAddress=[ip_address], SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway])


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
