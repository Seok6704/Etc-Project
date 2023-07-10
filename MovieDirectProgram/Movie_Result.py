from asyncio.windows_events import NULL
import requests
from bs4 import BeautifulSoup

def Movie_Result(text):
    Search_title = text

    link = requests.get('https://movie.naver.com/movie/search/result.naver?query=' + Search_title +'&section=all&ie=utf8') #네이버 영화 검색시 주소 명칭 규칙 이용
    html_doc = link.text

    soup = BeautifulSoup(html_doc, 'html.parser')

    title = soup.findAll("dt")
    length = len(title) # title 갯수 체크
    error = soup.find("ul", {"class" : "search_list_1"}) # 검색 결과가 없을 경우 None이 error에 담김
    if error!=None :
        return title, length
    else :
        return 0, 0
    