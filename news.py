import requests
from bs4 import BeautifulSoup

#bbc食品、健康
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

#yahoo健康新聞
def yahoo_health_news():
    yahoo_news = []
    url = 'https://tw.news.yahoo.com/health/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = soup.find_all('a', class_='D(ib) Ov(h) Whs(nw) C($c-fuji-grey-l) C($c-fuji-blue-1-c):h Td(n) Fz(16px) Tov(e) Fw(700)')[:5]
    for news_item in news_list:
        title = news_item.text.strip()
        link = news_item.get('href')
        yahoo_news.append({'title': title, 'link': link})
    return yahoo_news
    
#健身運動科學研究
def sport_science_news():
    sport_news = []
    url = 'https://www.sportscience.com.tw/article?Sort=1'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = soup.find_all('a', class_='articlelist__title-link')[:5]
    for news_item in news_list:
        title = news_item.text.strip()
        link = news_item.get('href')
        sport_news.append({'title': title, 'link': link})
    return sport_news
