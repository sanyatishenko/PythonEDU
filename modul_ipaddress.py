#! /usr/bin/env python3.6


import ipaddress
import sys

############################################################
#		Validation IP or Network
############################################################
net_str = '''
It's Network: {}
Network mask: {} prefix: {}
Maximum addresses: {}
Broadcast address: {}
'''
try:
	ipadd = ipaddress.ip_address(sys.argv[1])
except IndexError:
	print('Argument not found')
except ValueError:
	print('IP address not valid')
	try:
		net = ipaddress.ip_network(sys.argv[1])
	except ValueError:
		print('Network not valid')
	else:
		print(net_str.format(net.network_address,
 				     net.with_netmask,
				     net.prefixlen,
				     net.num_addresses,
				     net.broadcast_address))
else:
	print('It is IP addres: {} '.format(ipadd))

###########################################################
# 		Demo network metods
###########################################################
net_address = '172.31.1.0/28'

net = ipaddress.ip_network(net_address)
print('All addresses in network {}:'.format(net))
[print(ip) for ip in net] 

print('Subnets in this network:')
print(list(net.subnets()))
print('Subnets in this network prefix 29')
print(list(net.subnets(new_prefix=29)))
print('Subnets in this network prefix 30')
print(list(net.subnets(new_prefix=30)))

ip1 = ipaddress.ip_address('172.31.1.3')
ip2 = ipaddress.ip_address('172.31.0.3')

print('Ip1 include in net:', ip1 in net)
print('Ip2 include in net:', ip2 in net)

int1 = ipaddress.ip_interface('192.168.1.1/24')
print('Interface IP:',int1.ip)
print('Interface Network:',int1.network)
print('Interface Mask:',int1.netmask)



