''' IP scheduler '''


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
