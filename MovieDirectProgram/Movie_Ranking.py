import requests
from bs4 import BeautifulSoup

def movie_ranking() :
    link = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver')
    html_doc = link.text

    soup = BeautifulSoup(html_doc, 'html.parser')

    title = soup.findAll("div", {"class" : "tit3"})

    lenth = len(title)

    '''for n in range (0, lenth) :
        a = n + 1
        movie_title = title[n].a.text
        print(str(a) + " : " + movie_title)'''
    return lenth, title