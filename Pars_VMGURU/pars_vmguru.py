#! /usr/bin/env python3.6

import requests  
import re  
import sqlite3
import time
import os
import sys


def get_html(url):  
    '''Make request with URL, headers and 5 sec timeout  
       Function return html.text if status code eq. 200   
       and return 0 if code not eq. 200  
       requared import modules: requests, re'''
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}  
    timeout = 5  
    html = requests.get(url, headers = headers, timeout = timeout)  
    if html.status_code == 200:  
        regexp = r'<meta.+?charset=(\S+)?\"'  
        match = re.search(regexp,str(html.content))  
        html.encoding = match[1]  
        return html.text  
    else:  
        return 0  

# Возвращает число страниц новостей на сайте
def get_last_page(html):  
    '''find <a>-tag for last page with text &gt;&gt; and return number of last page        requared import modules: re'''  
    regexp = r'<a.+?(\d+)\">&gt;&gt;<\/a>'  
    match = re.search(regexp,html)  
    return(int(match[1]))


# Нахожит в HTML коде заголовки постов и возвращает в виде списка словарей с сылкой, заголовком и датой публикации
def get_posts(html): 
    '''function return all posts in html page 
       requared import modules: re''' 
    regexp = r'<a href=\"(?P<link>/.+)\">.*<h1 class=\"blog\">(?P<title>.+)<\/h1>.+>(?P<date>.+)</span>' 
    return([match.groupdict() for match in re.finditer(regexp,html)])


# Считывает указаное количество страниц сайта 
# и возвращает список словарей с сылкой, заголовком и датой публикации
def red_last_news(count):
	title_list = []
	sleep = 2
	for i in range(1,count+1):                              
		url = f'https://www.vmgu.ru/news/all/{i}' 
		html = get_html(url)                      
		title_list += get_posts(html)
		time.sleep(sleep)
	return(title_list)


# Выполняем скрипт создания БД из файла схемы                            
def create_db(dbname,file_schema):
	'''create database and tables'''
	connection = sqlite3.connect(dbname) 
	with open(file_schema,'r') as f:
		schema = f.read()
		connection.executescript(schema)
	connection.commit() 
	connection.close()



# Добавляет из списка в БД посты котрые еще не добавлены в БД
# возвращает список добавленных новостей
def add_posts(dbname,title_list):
	insert_query = '''INSERT INTO news (link,title,post_date,add_time) 
			  VALUES(:link,:title,:date,datetime('now'))'''   
	select_query = '''SELECT * FROM news WHERE link = :link'''        
	connection = sqlite3.connect(dbname)
	cursor = connection.cursor()
	add_news = []
	for row in title_list:
		# Приводим ссылку и дату публикации в нужный формат
		row['date'] = '{}-{}-{}'.format(row['date'][6:],row['date'][3:5],row['date'][0:2])
		row['link'] = f'https://vmgu.ru{row["link"]}'                       
		result = cursor.execute(select_query,row)
		result = cursor.fetchone()
		if not result:
			connection.execute(insert_query,row)
			add_news.append(row)
	connection.commit()
	connection.close()
	return(add_news)


# Проверка существование базы данных
# Если базы нет, ищем файл схемы и создаем БД
def check_db(db_file,schema_file):
	'''Function check DB. If all OK return 0, if DB created 1, if error 10'''
	print('Begin check DB ...')
	db_exists = os.path.exists(db_file)
	if not db_exists:
		print('DB {} not exists.'.format(db_file))
		schema_exists = os.path.exists(schema_file)
		if not schema_exists:
			print('Error! DB {} and schema {} files not exists!'.format(db_file,schema_file))
			return(10)
		else:
			print('Create DB {} from schema {}...'.format(db_file,schema_file))
			create_db(db_file,schema_file)
			return(1)
	print('End check DB: DB - exists!')
	return(0)



if __name__ == '__main__':
	dbname = 'vmguru.db'
	schema = 'schema.sql'
	count = 2 # Число страниц на которых ищем последнии новости
	mode  = check_db(dbname,schema)
	if mode == 10:
		print('Database Error!')
		sys.exit(10)
	elif mode == 1:
		# Режим создания базы - вычетка всех постов
		url = f'https://www.vmgu.ru/news'
		html = get_html(url)
		count = get_last_page(html)
		print(count)
	elif mode == 0:
		# Режим отслеживания новых постов
		pass
	else:
		print('Error! Unknowe mode.')
		sys.exit(10)

	title_list = red_last_news(count)
	add_news = add_posts(dbname,title_list)
	print('Add news count:',len(add_news))





'''
# Проверяем существование таблицы
def check_tables(db_file):
	'Function check tables in DB'
	print('Test connection to DB: {}'.format(db_file))
	connection = sqlite3.connect(db_file)
	cursor = connection.cursor()
	check_query = "SELECT name FROM sqlite_master WHERE type='table' AND name = 'news'"
	result = cursor.execute(check_query)
	result = cursor.fetchone()
	if not result:
		print('Error! Table "news" not found in DB {} !!!'.format(db_file))
		return(10)
	else:
		print('All OK!')
		return(0)


'''
