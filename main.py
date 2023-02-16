import requests
from bs4 import BeautifulSoup
import json


HOST = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273'
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}


def get_html(url, heagers):
    response = requests.get(url, headers=heagers)
    return response.text


def get_card(url):
    soup = BeautifulSoup(url, 'lxml')
    card_data = soup.find_all('div', class_="search-item regular-ad")
    return card_data
    
    


def card_info(soup):
    list_ = []
    for card in soup:
        title = card.find('div', class_="info").find('div', class_="title").find('a', class_ = 'title').text
        image = card.find('div', class_='left-col').find('picture').find('img').get('data-src')
        price = card.find('div', class_="price").text
        obj = {
            'title': title.strip(),
            'image': image,
            'price': price.strip()
        }
        list_.append(obj)
        y = json.dumps(obj)
    return y


def main():
    html = get_html(HOST, HEADERS)
    card = get_card(html)
    card_i = card_info(card)
    print(card_i)

main()