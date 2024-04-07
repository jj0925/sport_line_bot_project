import requests
from bs4 import BeautifulSoup

def bbc_food_healthy():
    bbc_news = []
    url = 'https://www.bbc.com/zhongwen/trad/topics/cezw73815zkt'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = soup.find_all('a', class_='focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0')[:5]
    for news_item in news_list:
        title = news_item.text.strip()
        link = news_item.get('href')
        bbc_news.append({'title': title, 'link': link})
    return bbc_news

