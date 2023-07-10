import requests
from bs4 import BeautifulSoup

def current_movie() :
    link = requests.get('https://movie.naver.com/movie/running/current.naver#')
    html_doc = link.text

    soup = BeautifulSoup(html_doc, 'html.parser')

    title = soup.findAll("dt", {"class" : "tit"})

    lenth = len(title)

    '''for n in range (0, lenth) :
        movie_title = title[n].a.text
        print("제목 : " + movie_title)'''
    return lenth, title