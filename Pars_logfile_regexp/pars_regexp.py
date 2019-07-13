######################################################
# Парсинг файла логов с помощью регулярных выражений
######################################################

import re

file_path = r"D:\GIT\PythonEDU\Pars_logfile_regexp\service_update.log"
f = open(file_path,'r')
text = f.read().split('\n')

x = []

for string in text:
    s = re.search('Service update version',string)
    if s:
        date = re.search(r'\d\d\d\d\D\d\d\D\d\d',string)
        version = re.search(r'(\d*\.\d*){3}',string)
        x.append({'Date' : date[0], 'Version' : version[0]})


for i,item in enumerate(x):
        if i == 0:
                print(x[i])
        else:
                if item['Version'] != x[i-1]['Version']:
                        print(item)




#print(len(x))
#print(x)

f.close()