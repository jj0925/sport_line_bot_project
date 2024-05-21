import requests
from bs4 import BeautifulSoup

def underweight_links():
    links = [
        "https://www.youtube.com/watch?v=XOrXz6c-EGg",
        "https://www.youtube.com/watch?v=BaFIqIQZDAs",
        "https://health.ltn.com.tw/article/breakingnews/3631647"
    ]
    return links
  
def normal_links():
    links = [
        "https://www.youtube.com/watch?v=k1xTzcfOsZg",
        "https://www.biojoy.com.tw/blogs/health/85905"
    ]
    return links

def overweight_links():
    links = [
        "https://www.youtube.com/watch?v=Tx5n1CvGkNk",
        "https://www.youtube.com/watch?v=X85DIStMn0I",
        "https://www.womenshealthmag.com/tw/fitness/work-outs/g46952096/lose-weight-exercise-workout-1708844375/"
    ]
    return links
  
def fetch_bmi_news():
    url = 'https://news.ltn.com.tw/topic/BMI'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news = soup.find_all('a', class_='tit')[:5]
    news_list = []
    for n in news:
        link = n.get('href')
        description = n.get('data-desc')
        news_list.append((description, link))
    return news_list


