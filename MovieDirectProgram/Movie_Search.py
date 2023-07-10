import requests
from bs4 import BeautifulSoup

def movie_search(text) :
    a = text
    flag = False # 찾는 장르가 있는지 검사할 변수
    #print("'" + a + "'장르의 영화를 탐색중입니다.")

    link = requests.get('https://movie.naver.com/movie/running/current.naver#')
    html_doc = link.text

    soup = BeautifulSoup(html_doc, 'html.parser')

    movie = soup.select("dl.lst_dsc") # soup 안에 html 성분중 dl.lst_dsc 아래에 성분을 모두 movie 변수 안에 저장.

    '''for m in movie : #moive 안에 있는 m의 숫자만큼 반복
        movie_genre = m.select("dl.info_txt1 dd:nth-of-type(1) a") #dl >> info_txt1 >> dd 안에서 nth-of-type(1). 첫번째로 만나는 a로 시작하는 성분을 모두 변수에 저장.
        movie_title = m.select_one("dt.tit a").text #dt >> tit >> a 로 시작하는 성분을 변수안에 단일로 저장
        for g in movie_genre:
            if a in g.text : #입력 받은 장르가 movie_genre의 텍스트 성분에 포함될경우 출력
                print("제목 : " + movie_title)
                flag = True
    if flag == False : #찾는 장르가 하나도 없는 경우
        print("찾으시는 장르가 없습니다.")'''

    return movie, flag
