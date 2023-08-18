# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


import content_based
from content_based import content_rec, df
from collab_filter import collab_filter
import json
import pandas as pd
from ast import literal_eval
from scrollableLabel import scrollLabel

# with open("mydata.json", encoding="utf8") as f:
#     data = literal_eval(f.read())
# i = 0
# for d in data:
#     d['index'] = i
#     i += 1
# # print(data)
# df = pd.json_normalize(data)
# print(df)


# list of tuples(movie, index)
favMovies = []  # name, index, rating
content_rec_movies = []
selectedFavMovieIndex = 0  # to set rating
result = []


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 852)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.searchArea = QtWidgets.QTextEdit(self.centralwidget)
        self.searchArea.setGeometry(QtCore.QRect(50, 60, 261, 31))
        self.searchArea.setObjectName("searchArea")
        self.searchArea.setPlaceholderText("Search Movie")
        self.searchArea.textChanged.connect(self.searchTermUpdate)

        self.showAllList()
        self.ShowAlllistWidget.currentRowChanged.connect(self.ShowSelected1)

        self.ShowSelectList()
        self.addMovieButton()
        self.RecommList()

        self.ShowReclistWidget.currentRowChanged.connect(self.ShowDetails)

        self.recommend_button = QtWidgets.QPushButton(self.centralwidget)
        self.recommend_button.setGeometry(QtCore.QRect(320, 540, 251, 41))
        self.recommend_button.setText("")
        self.recommend_button.setObjectName("recommend_button")
        self.recommend_button.clicked.connect(self.RecommMovies)
        # self.RecButlabel = QtWidgets.QLabel(self.centralwidget)
        # self.RecButlabel.setGeometry(QtCore.QRect(330, 530, 231, 61))
        # self.RecButlabel.setObjectName("RecButlabel")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(640, 350, 421, 351))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 419, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.titleLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(19)
        self.titleLabel.setFont(font)
        self.titleLabel.setText("")
        self.titleLabel.setObjectName("titleLabel")
        self.descriptionLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.descriptionLabel.setGeometry(QtCore.QRect(4, 145, 411, 221))
        self.descriptionLabel.setText("")
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.descriptionLabel.setWordWrap(True)

        self.genreLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.genreLabel.setGeometry(QtCore.QRect(0, 90, 421, 31))
        self.genreLabel.setText("")
        self.genreLabel.setObjectName("genreLabel")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(650, 720, 431, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.ratingSelector = QtWidgets.QSpinBox(self.centralwidget)
        self.ratingSelector.setGeometry(QtCore.QRect(540, 730, 42, 22))
        self.ratingSelector.setObjectName("ratingSelector")
        self.ratingSelector.valueChanged.connect(self.setRating)

        self.ratingMovie = QtWidgets.QLabel(self.centralwidget)
        self.ratingMovie.setGeometry(QtCore.QRect(350, 706, 171, 61))
        self.ratingMovie.setText("")
        self.ratingMovie.setObjectName("ratingMovie")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 670, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.recommend_button_user = QtWidgets.QPushButton(self.centralwidget)
        self.recommend_button_user.setGeometry(QtCore.QRect(320, 600, 251, 41))
        self.recommend_button_user.setText("")
        self.recommend_button_user.setObjectName("recommend_button_user")
        self.recommend_button_user.clicked.connect(self.RecommMoviesCollab)
        # self.RecButlabel_2 = QtWidgets.QLabel(self.centralwidget)
        # self.RecButlabel_2.setGeometry(QtCore.QRect(330, 590, 231, 61))
        # self.RecButlabel_2.setObjectName("RecButlabel_2")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(644, 50, 411, 261))
        self.image.setText("")
        self.image.setScaledContents(True)
        self.image.setObjectName("image")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Selected1.setText(_translate("MainWindow", "Selected Movie"))
        self.pushButton_Add.setText(_translate("MainWindow", "Add"))
        self.pushButton_remove.setText(_translate("MainWindow", "Remove"))
        self.Selected2.setText(_translate("MainWindow", "Selected Movie"))
        self.Recommended.setText(_translate("MainWindow", "Recommended"))
        # self.RecButlabel.setText(_translate("MainWindow", "Recommend based on selected movie"))
        self.label_2.setText(_translate(
            "MainWindow", "Select your rating for this movie"))
        self.recommend_button.setText(_translate(
            "MainWindow", "Recommend based on selected movie"))
        self.recommend_button_user.setText(_translate(
            "MainWindow", "Recommend based on collab filter"))
        # self.RecButlabel_2.setText(_translate("MainWindow", "Recommend based on collab filter"))

    ############################################################################

    def showAllList(self):
        self.ShowAlllistWidget = QtWidgets.QListWidget(self.centralwidget)
        self.ShowAlllistWidget.setGeometry(QtCore.QRect(50, 110, 261, 331))
        self.ShowAlllistWidget.setObjectName("ShowAlllistWidget")
        for mov in df["title"]:
            QtWidgets.QListWidgetItem(mov, self.ShowAlllistWidget)

        self.Selected1 = QtWidgets.QLabel(self.centralwidget)
        self.Selected1.setGeometry(QtCore.QRect(50, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Selected1.setFont(font)
        self.Selected1.setObjectName("Selected1")
        self.Selected1.setWordWrap(True)

    # for label above showall
    def ShowSelected1(self):
        if(self.ShowAlllistWidget.currentRow() >= 0):
            self.Selected1.setText(
                df["title"][self.ShowAlllistWidget.currentRow()])
            self.Selected1.adjustSize()

    # to show favourites list
    def ShowSelectList(self):
        self.ShowFavlistWidget = QtWidgets.QListWidget(self.centralwidget)
        self.ShowFavlistWidget.setGeometry(QtCore.QRect(50, 490, 261, 241))
        self.ShowFavlistWidget.setObjectName("ShowFavlistWidget")
        for mov in favMovies:
            QtWidgets.QListWidgetItem(mov[0], self.ShowFavlistWidget)
        self.pushButton_remove = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_remove.setGeometry(QtCore.QRect(210, 750, 93, 28))
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.pushButton_remove.clicked.connect(self.RemoveMovie)
        self.Selected2 = QtWidgets.QLabel(self.centralwidget)
        self.Selected2.setGeometry(QtCore.QRect(320, 490, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Selected2.setFont(font)
        self.Selected2.setObjectName("Selected2")
        self.ShowFavlistWidget.currentRowChanged.connect(self.ShowFavRating)

    def searchTermUpdate(self):
        searchText = self.searchArea.toPlainText()
        print(searchText)




    def ShowFavRating(self):
        if(self.ShowFavlistWidget.currentRow() >= 0):
            self.ratingMovie.setText(
                df["title"][favMovies[self.ShowFavlistWidget.currentRow()][1]])
            if self.ShowFavlistWidget.currentRow() < len(favMovies):
                self.ratingSelector.setValue(
                    favMovies[self.ShowFavlistWidget.currentRow()][2])
            self.ratingMovie.adjustSize()

    def setRating(self):

        rating = self.ratingSelector.value()
        if self.ShowFavlistWidget.currentRow() < len(favMovies):
            favMovies[self.ShowFavlistWidget.currentRow()][2] = rating

    def addMovieButton(self):
        self.pushButton_Add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Add.setGeometry(QtCore.QRect(220, 450, 93, 28))
        self.pushButton_Add.setObjectName("pushButton_Add")
        self.pushButton_Add.clicked.connect(self.AddMovie)

    def AddMovie(self):
        if(self.ShowAlllistWidget.currentRow() >= 0):
            index = (self.ShowAlllistWidget.currentRow())
            name = df["title"][(self.ShowAlllistWidget.currentRow())]
            if (name, index) not in favMovies:
                favMovies.append([name, index, 0])
                QtWidgets.QListWidgetItem(name, self.ShowFavlistWidget)
                # print(favMovies)

    def RemoveMovie(self):
        if(self.ShowFavlistWidget.currentRow() >= 0):
            index = (self.ShowFavlistWidget.currentRow())
            # print(index)
            name = df["title"][(self.ShowFavlistWidget.currentRow())]
            favMovies.pop(index)
            self.ShowFavlistWidget.takeItem(index)
            # print(favMovies)

    def RecommList(self):
        self.ShowReclistWidget = QtWidgets.QListWidget(self.centralwidget)
        self.ShowReclistWidget.setGeometry(QtCore.QRect(350, 60, 251, 381))
        self.ShowReclistWidget.setObjectName("ShowReclistWidget")
        for mov in content_rec_movies:
            QtWidgets.QListWidgetItem(mov[0], self.ShowFavlistWidget)
        self.Recommended = QtWidgets.QLabel(self.centralwidget)
        self.Recommended.setGeometry(QtCore.QRect(350, 20, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Recommended.setFont(font)
        self.Recommended.setObjectName("Recommended")

    def RecommMovies(self):
        if self.ShowFavlistWidget.currentRow() == -1:
            return
        self.ShowReclistWidget.clear()
        name, index, rating = favMovies[self.ShowFavlistWidget.currentRow()]
        global content_rec_movies
        content_rec_movies = []
        content_rec_movies = content_based.content_rec(  # tuple of moviename and index in df
            df["title"][index])
        print(content_rec_movies)
        for mov in content_rec_movies:
            QtWidgets.QListWidgetItem(mov[0], self.ShowReclistWidget)

    def RecommMoviesCollab(self):
        self.ShowReclistWidget.clear()
        global content_rec_movies
        content_rec_movies = []
        result = collab_filter(favMovies)
        # print(result)
        # need to get tuple of moviename and index in df
        i = 0
        for col in result.columns:
            col = int(col)
            print("lol")
            print(col)
            content_rec_movies.append((df["title"][col-1], col-1))
            i += 1
            if(i > 50):
                break
        print(content_rec_movies)
        for mov in content_rec_movies:
            QtWidgets.QListWidgetItem(mov[0], self.ShowReclistWidget)

    def ShowDetails(self):

        if(self.ShowReclistWidget.currentRow() >= 0):
            # getting index of movie
            # print(content_rec_movies)

            index = content_rec_movies[self.ShowReclistWidget.currentRow()][1]
            title = content_rec_movies[self.ShowReclistWidget.currentRow()][0]

            # print(df)

            self.titleLabel.setText(title)
            self.titleLabel.adjustSize()
            self.descriptionLabel.setText(df["description"][index])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())