import requests
from bs4 import BeautifulSoup
import json


def get_html(url, heagers):
    response = requests.get(url, headers=heagers)
    return response.text


def get_card(url):
    soup = BeautifulSoup(url, 'lxml')
    card_data = soup.find_all('div', class_="search-item regular-ad")
    return card_data


def card_info(soup, page):
    list_ = []
    for card in soup:
        title = card.find('div', class_="info").find('div', class_="title").find('a', class_ = 'title').text
        try:
            image = card.find('div', class_='left-col').find('picture').find('img').get('data-src')
        except AttributeError:
            image = None
        price = card.find('div', class_="price").text
        obj = {
            'title': title.strip(),
            'image': image,
            'price': price.strip(),
            'page': page
        }
        list_.append(obj)
    return list_




def write_AIDAR(obj):
    with open(file='aidar1.json', mode='w') as file:
        json.dump(obj=obj, fp=file, indent=4)
def main():
    list_ = []
    for i in range(5):
        HOST = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{i+1}/c37l1700273?ad=offering'
        HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
        html = get_html(url=HOST, heagers=HEADERS)
        card = get_card(url=html)
        card_i = card_info(card, page=i+1)
        list_.extend(card_i)
        write_AIDAR(list_)
    return list_
        

if __name__ == '__main__':
    print(main())