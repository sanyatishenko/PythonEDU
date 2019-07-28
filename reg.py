#! /usr/bin/env python3.6


import os
import re


regexp = r'(\\\S+?\\)(\S+?)\\(.*\\)?(\S+)\\(\S+\.vhd.?)\s+(\d+)'

dict_key = ['Volume','VM','Disk','Size']

main_path = os.path.abspath('.')
file_path = os.path.join(main_path,'files','disks.txt')

if os.path.exists(file_path):
	with open(file_path,'r') as f:
		for line in f:
			match = re.search(regexp,line)
			if match:
				result = dict(zip(dict_key,match.group(2,4,5,6)))
				print(result)


