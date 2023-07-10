import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont

#Ui 파일 import
from MovieUI_v2 import *
import Current_Movie as CM
import Movie_Ranking as MR
import Movie_Search as MS
import Movie_Result as MRES

# 프로그램 메인 UI 실행 클래스
class MainClass(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.main = Ui_MainWindow() # UI 선언
        self.main.setupUi(self)   #UI 준비
        self.main.textEdit.setFont(QFont("contras", 12)) #textEdit 폰트 설정 contras 12px
        self.main.textEdit.setText("ex) 로맨스, 액션, 스릴러..") #textEdit 텍스트 설정
        self.main.MB_1.clicked.connect(self.MB_1_Clicked) #MB_1 클릭시 함수 호출
        self.main.MB_2.clicked.connect(self.MB_2_Clicked) #MB_2 클릭시 함수 호출
        self.main.MB_3.clicked.connect(self.MB_3_Clicked) #MB_3 클릭시 함수 호출
        self.main.MB_4.clicked.connect(self.MB_4_Clicked) #MB_4 클릭시 함수 호출
        self.show() # 화면 출력
    
    def Result_Clear(self): #Result_Box 초기화 함수
        self.main.Result_Box.clear()

    def MB_1_Clicked(self):
        self.Result_Clear()
        lenth, title = CM.current_movie()
        for n in range (0, lenth) :
            movie_title = title[n].a.text
            self.main.Result_Box.append("제목 : " + movie_title)

    def MB_2_Clicked(self):
        self.Result_Clear()
        lenth, title = MR.movie_ranking()
        for n in range (0, lenth):
            a = n + 1
            movie_title = title[n].a.text
            self.main.Result_Box.append(str(a) + " : " + movie_title)

    def MB_3_Clicked(self):
        self.Result_Clear()
        self.text = self.main.textEdit.toPlainText() #textEdit 박스 안에 있는 텍스트 변수 저장
        movie, flag = MS.movie_search(self.text)
        for m in movie : #moive 안에 있는 m의 숫자만큼 반복
            movie_genre = m.select("dl.info_txt1 dd:nth-of-type(1) a") #dl >> info_txt1 >> dd 안에서 nth-of-type(1). 첫번째로 만나는 a로 시작하는 성분을 모두 변수에 저장.
            movie_title = m.select_one("dt.tit a").text #dt >> tit >> a 로 시작하는 성분을 변수안에 단일로 저장
            for g in movie_genre:
                if self.text in g.text : #입력 받은 장르가 movie_genre의 텍스트 성분에 포함될경우 출력
                 self.main.Result_Box.append("제목 : " + movie_title)
                 flag = True
        if flag == False : #찾는 장르가 하나도 없는 경우
            self.main.Result_Box.append("찾으시는 장르가 없습니다.")

    def MB_4_Clicked(self):
        self.Result_Clear()
        self.text = self.main.textEdit_2.toPlainText()
        title, length = MRES.Movie_Result(self.text)
        if title == 0 : # 검색결과가 없었을 경우
            self.main.Result_Box.append("검색 결과가 없습니다. 제목을 정확하게 입력해주세요.")
        else : #검색결과가 있는 경우
            if length > 5 : # 네이버 영화 기준으로 영화 검색 결과 숫자는 최대 5개, 5개를 넘을경우 5개까지만 출력, 아닐경우 length 길이 그대로 출력.
                length = 5
            for n in range (0, length):
                a = n + 1
                movie_title = title[n].a.text
                self.main.Result_Box.append(str(a) + " : " + movie_title)
            self.main.Result_Box.append("검색 결과입니다. 원하시는 영화의 번호를 입력해 주세요.")
            self.main.Result_Box.append("원하시는 결과가 없을 경우 제목을 좀 더 정확하게 입력해 주세요.")    


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = MainClass() # Mainclass 호출
    app.exec_()