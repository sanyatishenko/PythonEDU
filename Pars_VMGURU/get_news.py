################################################
# Список новостей с сайта https://www.vmgu.ru
################################################

import requests
from bs4 import BeautifulSoup
import codecs

def get_html(url):
    html = requests.get(url)
    if html.status_code == 200:
        html.encoding = 'windows-1251'
        return html.text
    else:
        return 0


def get_news(html):
    news = []
    soup = BeautifulSoup(html, "html.parser") 
    data = {}
    for item in soup.find_all('h1', {'class':'blog'}):

        for span in item.find_all('span'):
            data.update({'date' : span.text})

        for href in item.find_all('a'):
            data.update({'href' : href.get('href')})
            data.update({'text' : href.text})

        news.append(data.copy())
        
    return news



def main():
    url = "https://www.vmgu.ru"
    html = get_html(url)
    if html:
        news = get_news(html)
                       
        for item in news:
            if item :        
                print(item['date'])    
                print(item['text'])
                print(url+item['href'])
        




if __name__ == '__main__' :
    main()        
