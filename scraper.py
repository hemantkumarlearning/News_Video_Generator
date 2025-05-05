import requests
from bs4 import BeautifulSoup

def trending_news():
    url="https://www.indiatoday.in"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")
    articles = soup.select('h2 a')[:5]
    headlines = [a.text.strip() for a in articles if a.text.strip()]
    return headlines