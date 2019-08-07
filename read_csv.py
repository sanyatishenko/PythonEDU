#! /usr/bin/env python3.6


import csv
import os 


current_path = os.path.abspath('.')
file_path = os.path.join(current_path,'files','vm_data')
csv_file_list = [f.path for f in os.scandir(file_path) if (f.is_file() and f.name[-4:] == '.csv')]
print(csv_file_list)

path = csv_file_list[0]

# Чтение CSV построчно в список списков
with open(path) as f:
	row = csv.reader(f, delimiter=';')
	headers = next(row)
	print('Headers:',headers)
	for line in row:
		print(line)
'''
['VM;Size;FileSize;Path']
['V-ADDS01;80;80;C:\\ClusterStorage\\Volume1\\V-ADDS01_disk1']
['V-PKI01;80;40;C:\\ClusterStorage\\Volume1\\V-PKI01_disk1']
['V-DHCP01;80;40;C:\\ClusterStorage\\Volume1\\V-DHCP01_disk1']
'''

# Чтение CSV в список словарей
with open(path) as f:
	data = csv.DictReader(f, delimiter=';')
	for line in data:
		print(line)


