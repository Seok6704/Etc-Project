# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MovieUI_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1077, 719)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Menu_box_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.Menu_box_1.setGeometry(QtCore.QRect(10, 20, 381, 31))
        self.Menu_box_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Menu_box_1.setObjectName("Menu_box_1")
        self.Menu_box_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.Menu_box_2.setGeometry(QtCore.QRect(10, 70, 381, 31))
        self.Menu_box_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Menu_box_2.setObjectName("Menu_box_2")
        self.Menu_box_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.Menu_box_3.setGeometry(QtCore.QRect(480, 20, 311, 41))
        self.Menu_box_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Menu_box_3.setObjectName("Menu_box_3")
        self.MB_1 = QtWidgets.QPushButton(self.centralwidget)
        self.MB_1.setGeometry(QtCore.QRect(400, 20, 71, 31))
        self.MB_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Consolas\";")
        self.MB_1.setObjectName("MB_1")
        self.MB_2 = QtWidgets.QPushButton(self.centralwidget)
        self.MB_2.setGeometry(QtCore.QRect(400, 70, 71, 31))
        self.MB_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Consolas\";")
        self.MB_2.setObjectName("MB_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(480, 70, 251, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.MB_3 = QtWidgets.QPushButton(self.centralwidget)
        self.MB_3.setGeometry(QtCore.QRect(740, 70, 51, 31))
        self.MB_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 9pt \"Consolas\";")
        self.MB_3.setObjectName("MB_3")
        self.Result_Box = QtWidgets.QTextEdit(self.centralwidget)
        self.Result_Box.setGeometry(QtCore.QRect(400, 110, 661, 561))
        self.Result_Box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Result_Box.setObjectName("Result_Box")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(800, 20, 201, 41))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.MB_4 = QtWidgets.QPushButton(self.centralwidget)
        self.MB_4.setGeometry(QtCore.QRect(1010, 20, 61, 41))
        self.MB_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Consolas\";")
        self.MB_4.setObjectName("MB_4")
        self.Img_label = QtWidgets.QLabel(self.centralwidget)
        self.Img_label.setGeometry(QtCore.QRect(10, 110, 381, 551))
        self.Img_label.setText("")
        self.Img_label.setObjectName("Img_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1077, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MovieDirector V_2"))
        self.Menu_box_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">1. 현재 상영중인 영화 목록 불러오기</span></p></body></html>"))
        self.Menu_box_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">2. 현재 상영중인 영화 순위 확인</span></p></body></html>"))
        self.Menu_box_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">추천 받으실 영화 장르를 입력해주세요. 상영중인 해당 장르 영화를 나열합니다.</span></p></body></html>"))
        self.MB_1.setText(_translate("MainWindow", "Start"))
        self.MB_2.setText(_translate("MainWindow", "Start"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.MB_3.setText(_translate("MainWindow", "검색"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">영화 제목을 입력해주세요. 아래에 영화 정보가 출력됩니다.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.MB_4.setText(_translate("MainWindow", "검색"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
