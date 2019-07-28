#! /usr/bin/env python3.6


###############################################################
# Синтаксис регулянных выражений, группы вхождения
# http://www.pyregex.com
# https://regex101.com
###############################################################


import os
import re


main_path = os.path.abspath('.')
file_path = os.path.join(main_path,'files','disks.txt')

# () - захватывает выражение в группе и возвращает его в match.group(i) match.groups()
#match.group(0) - возвращает все совпадение
#match.group(1) - возвращает первую найденую группу
#match.groups() - возвращает кортеж со всеми группами
regexp = r'(\\\S+?\\)(\S+?)\\(.*\\)?(\S+)\\(\S+\.vhd.?)\s+(\d+)'

# (?P<Key>RegExp) - задает имя группы которе является ключом для match.groupsdict()
# 					или ключом при обрщении к match.groups('Key')
# (:?RegExp) - не добовляет группу в match.groups()
# \1 - повторение группы 1  # 'qwerty qwerty' => r'(\S+) \1'
regexp2 = r'(?:\\\S+?\\)(?P<Volume>\S+?)\\(?:.*\\)?(?P<VM>\S+)\\(?P<Disk>\S+\.vhd.?)\s+(?P<Size>\d+)'


# match.search() - возвращает первое вхождение регулярного выражения
def pars1(file_path,regexp):
	dict_key = ['Volume','VM','Disk','Size']
	if os.path.exists(file_path):
		with open(file_path,'r') as f:
			for line in f:
				match = re.search(regexp,line)
				if match:
					print(dict(zip(dict_key,match.group(2,4,5,6))))
				
# match.groupdict() - возвращает словать с ключаи из ?P<>
def pars2(file_path,regexp):
	if os.path.exists(file_path):
		with open(file_path,'r') as f:
			for line in f:
				match = re.search(regexp,line)
				if match:
					print(match.groupdict()) 
					

# re.finditer() - возвращает итерируемый объект со всеми совпадениями
def pars3(file_path,regexp):			
	if os.path.exists(file_path):
		with open(file_path,'r') as f:
			print([match.groupdict() for match in re.finditer(regexp,f.read())])
			#result = re.finditer(regexp,f.read())
			#for match in result:
			#	print(match.groupdict())

# re.findall() - находит все вхождения и в зависимости от регулярного выражения
# 				 возвращает разные значения
# Если в регулярном выражении нет групп () возвращает список строк в котрых есть вхождение
# Если в выражении одна группа (), то возвращает список строк с единственной группой
# Если в выражении несколько групп () (), то возвращает список кортежей
def pars4(file_path,regexp):
	if os.path.exists(file_path):
			with open(file_path,'r') as f:
				print(re.findall(regexp,f.read()))



# re.compile() - создает объект регулярного выражения, у котроге есть меторы
#				 search и др. Ожидает на вход строку.
def pars5(file_path,regexp):
	r = re.compile(regexp)
	if os.path.exists(file_path):
		with open(file_path,'r') as f:
			for line in f:
				match = r.search(line)
				if match:
					print(match.groupdict()) 


string='''DNS-суффикс подключения . . . . . : localhost
   Описание. . . . . . . . . . . . . : Qualcomm Atheros AR9285 Wireless Network
   Физический адрес. . . . . . . . . : 1C-4B-D6-76-AD-8F
   DHCP включен. . . . . . . . . . . : Да
   Автонастройка включена. . . . . . : Да
   Локальный IPv6-адрес канала . . . : fe80::ecb5:e210:861e:4d9e%4(Основной)
   IPv4-адрес. . . . . . . . . . . . : 192.168.1.10(Основной)
   Маска подсети . . . . . . . . . . : 255.255.255.0
   Аренда получена. . . . . . . . . . : 28 июля 2019 г. 11:54:48
   Срок аренды истекает. . . . . . . . . . : 4 сентября 2155 г. 2:46:34
   Основной шлюз. . . . . . . . . : 192.168.1.1
   DHCP-сервер. . . . . . . . . . . : 192.168.1.1'''
# re.split() разбивает строку по регулярному выражению
def pars6(string):
	print('-'*30)
	for line in string.split('\n'):		
		print(re.split(r' ?(?:\.\s)+: ?',line.strip()))
			

# re.sub() заменяет подстроку по регулярному выражению
def pars7(string):
	print('-'*30)
	print(re.sub(r'(?:\s+)?'			# последовательность пробелов в начале строки(?: не запоминаем) 
					r'(.*?)'			# все что до многоточия, группа будет под №1
					r'(?:\.\s)+:\s+'	# последовательность точек и пробелов (?: не запоминаем)
					r'(.+)',			# все что после двоеточия, группа будет под №2
					r'\1 \2\n',
					string))

print("#"*30)
pars1(file_path,regexp)
print("#"*30)
pars2(file_path,regexp2)
print("#"*30)
pars3(file_path,regexp2)
print("#"*30)
pars4(file_path,regexp2)
print("#"*30)
pars5(file_path,regexp2)

print(string.strip())
print("#"*30)
pars6(string)
print("#"*30)
pars7(string)