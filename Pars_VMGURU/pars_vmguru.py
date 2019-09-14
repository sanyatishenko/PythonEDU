import requests  
import re  
import sqlite3
import time
import os

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


def get_last_page(html):  
    '''find <a>-tag for last page with text &gt;&gt; and return number of last page        requared import modules: re'''  
    regexp = r'<a.+?(\d+)\">&gt;&gt;<\/a>'  
    match = re.search(regexp,html)  
    return(match[1])

  
def get_posts(html): 
    '''function return all posts in html page 
       requared import modules: re''' 
    regexp = r'<a href=\"(?P<link>/.+)\">.*<h1 class=\"blog\">(?P<title>.+)<\/h1>.+>(?P<date>.+)</span>' 
    return([match.groupdict() for match in re.finditer(regexp,html)])

def red_last_news(count):
	title_list = []
	sleep = 2
	for i in range(1,count):                              
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



def add_posts(dbname,title_list):
	insert_query = '''INSERT INTO news (link,title,post_date,add_time) 
			  VALUES(:link,:title,:date,datetime('now'))'''   
	select_query = '''SELECT * FROM news WHERE link = :link'''        
	connection = sqlite3.connect(dbname)
	cursor = connection.cursor()
	add_news = []
	for row in title_list:
		row['date'] = '{}-{}-{}'.format(row['date'][6:],row['date'][3:5],row['date'][0:2])
		row['link'] = f'https://vmgu.ru{row["link"]}'                       
		result = cursor.execute(select_query,row)
		result = cursor.fetchone()
		if not result:
			connection.execute(insert_query,row)
			add_news += row
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
	prin('End check DB: DB - exists!')
	return(0)


















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
