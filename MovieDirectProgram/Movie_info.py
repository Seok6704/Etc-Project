import requests
from bs4 import BeautifulSoup

link = requests.get('https://movie.naver.com/movie/bi/mi/basic.naver?code=182016')
html_doc = link.text

soup = BeautifulSoup(html_doc, 'html.parser')