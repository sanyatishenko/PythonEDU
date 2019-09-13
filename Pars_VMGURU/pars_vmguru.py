import requests  
import re  
import sqlite3

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


title_list = []                                     
for i in range(1,3):                              
        url = f'https://www.vmgu.ru/news/all/{i}' 
        html = get_html(url)                      
        title_list += get_posts(html)
                                                  


connection = sqlite3.connect('vmguru.db')
cursor = connection.cursor()
create_table_news = (r'CREATE TABLE IF NOT EXISTS news('
r'id INTEGER PRIMARY KEY,'
r'link text,'
r'title text,'
r'post_date DATE,'
r'add_time DATE)')

cursor.execute(create_table_news)

for row in title_list:
	query = '''INSERT INTO news (link,title,post_date,add_time)
		   VALUES(:link,:title,:date,datetime('now'))'''
	row['date'] = '{}-{}-{}'.format(row['date'][6:],row['date'][3:5],row['date'][0:2])
	connection.execute(query,row)


connection.commit()
connection.close()

# datetime('now')




'''
title_list=[]
for i in range(1,6):
	url = f'https://www.vmgu.ru/news/all/{i}'  
	html = get_html(url)
	title_list+=get_posts(html) 

print('title list len:',len(title_list))
'''
