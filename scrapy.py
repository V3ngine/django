import os
import json
from bs4 import BeautifulSoup
import requests
import lxml


URL = "http://books.toscrape.com/"

HEADERS = {

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    }


def get_links(url, headers):
   
    response = requests.get(url, headers)
    html = response.text
    
    with open('sa.html', 'w', encoding='utf-8') as file:
        file.write(html)

    soup = BeautifulSoup(html, 'lxml')
    conteiner = soup.find_all('div', class_='image_container')
    
    links = []

    for link in conteiner:
        href = URL + link.find('a').get('href')
        links.append(href)

    return links


def get_items(links,headers):

    data_items =[]
    iter = 0
    
    for link in links:
        iter += 1
        response = requests.get(link, headers).text
        soup = BeautifulSoup(response, 'lxml')
        img = soup.find('div', class_='item active').find('img').get('src')
        title = soup.find('div', class_='col-sm-6 product_main').find('h1').get_text('font')
        contents = soup.find('article').find_all('p')
        
        photo = f'{URL}{img}'

        pic =requests.get(photo).content
       
        if not os.path.exists('picture'):
                os.mkdir('picture')

        
        with open(f'picture/pic_{iter}.jpg', 'wb') as file:
                file.write(pic)

        for con in contents:
            content = con.get_text('font')
            if len(content)> 100:

                data_items.append(
                    {
                        'Название': title,
                        'Обложка': img,
                        'Контент': content,
                    }
                )

        print(f'Парсер загрузил статью : {iter} из 20 ')

    with open('data_items.json', 'w', encoding='utf8') as file:
        json.dump(data_items, file, ensure_ascii=False, indent=4)
    
   
    
    print(f'Парсер загрузил все статьи')
    



links = get_links(URL, HEADERS)
items = get_items(links, HEADERS)

