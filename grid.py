# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grid.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize
import requests
from searchFunctions import searchQuery
import content_based
from content_based import content_rec, df
from collab_filter import collab_filter
import json
import pandas as pd
from ast import literal_eval
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QListWidgetItem, QLabel
from PyQt5.QtGui import QPixmap, QIcon, QImage
import urllib


user_favs = []
initial = 1


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        self.selected_product = -1
        self.searchText = ''

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 40, 681, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText("Search Product")
        self.textEdit.textChanged.connect(self.searchTermUpdate)
        self.resultsScollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.resultsScollArea.setGeometry(QtCore.QRect(20, 100, 751, 471))
        self.resultsScollArea.setWidgetResizable(True)
        self.resultsScollArea.setObjectName("resultsScollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 749, 469))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(-5, 1, 761, 471))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemDoubleClicked.connect(self.showProduct)
        self.listWidget.setWordWrap(True)
        size = QSize()
        size.setHeight(100)

        self.resultsScollArea.setWidget(self.scrollAreaWidgetContents)
        global initial
        global user_favs
        if initial == 1 or len(user_favs) < 1:
            self.submitSearch()
        else:
            self.fetchCollab()
        initial = 0

        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(710, 40, 81, 31))
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.submitSearch)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Product Recommender"))
        self.searchButton.setText(_translate("MainWindow", "Search"))

    def fetchCollab(self):
        self.search_index_map = {}
        collab_results = collab_filter(user_favs)
        self.listWidget.clear()
        i = 0

        for column in collab_results.columns:
            if i > 50:
                break
            if column == 'productId':
                continue
            ind = int(column)
            self.listWidget.addItem(
                QListWidgetItem(df['product_name'][ind]))
            self.search_index_map[i] = id
            i += 1

    def searchTermUpdate(self):
        self.searchText = self.textEdit.toPlainText()
        print(self.searchText)

    def submitSearch(self):
        self.search_index_map = {}

        self.listWidget.clear()
        self.searchResults = searchQuery(self.searchText)
        print(self.searchResults)
        i = 0
        for ind in self.searchResults.index:
            if i > 50:
                break
            id = self.searchResults['index'][ind]
            name = self.searchResults['product_name'][ind] + '\n\n' + \
                self.searchResults['discounted_price'][ind] + \
                '\n\n' + 'Average Rating : ' + \
                str(self.searchResults['rating'][ind])
            name = name.replace('\u20b9', 'Rs. ')
            print(name)
            icon = QIcon('placeholder.png')
            listWidgetItem = QListWidgetItem(icon, name)

            self.listWidget.addItem(listWidgetItem)
            self.search_index_map[i] = id
            i += 1

    def showProduct(self):
        if self.listWidget.currentRow() >= 0:

            id = self.search_index_map[self.listWidget.currentRow()]

            self.selected_product = id
            content_results = content_rec(df['product_name'][id])
            collab_results = collab_filter([(df['product_name'][id], id, 5)])

            self.p_window = ProductWindow()
            self.p_window.setupUi(
                MainWindow, id, content_results, collab_results)

            print('lol')


class ProductWindow(QWidget):
    # def __init__(self, id):
    #     super().__init__()
    #     layout = QVBoxLayout()
    #     print(id)
    #     # layout.addWidget(self.label)
    #     self.setLayout(layout)

    def setupUi(self, MainWindow, id, content_results, collab_results):
        self.content_results = content_results
        self.collab_results = collab_results
        self.id = id
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.go_back)
        self.productImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.productImageLabel.setGeometry(QtCore.QRect(40, 70, 321, 211))
        self.productImageLabel.setText("")
        self.productImageLabel.setObjectName("productImageLabel")

        self.productImageLabel.setPixmap(QPixmap('placeholder.png'))
        print('lol')
        print(df['product_name'][id])
        self.productLabel = QtWidgets.QTextBrowser(self.centralwidget)
        self.productLabel.setObjectName(u"productLabel")
        self.productLabel.setGeometry(QtCore.QRect(400, 50, 371, 251))

        self.productLabel.setText(df['about_product'][id])
        self.productLabel.adjustSize()
        self.productTitle = QtWidgets.QLabel(self.centralwidget)
        self.productTitle.setObjectName("productTitle")
        self.productTitle.setGeometry(QtCore.QRect(118, 30, 661, 20))
        self.productTitle.setText(df['product_name'][id])
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 300, 49, 16))
        self.label.setObjectName("label")
        self.label.setText('Products Similiar to this')
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 440, 49, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setText('Customers who bought this also bought')
        self.contentBasedList = QtWidgets.QListWidget(self.centralwidget)
        self.contentBasedList.setGeometry(QtCore.QRect(30, 320, 741, 101))
        self.contentBasedList.setFlow(QtWidgets.QListView.LeftToRight)
        self.contentBasedList.setObjectName("contentBasedList")
        self.collabBasedList = QtWidgets.QListWidget(self.centralwidget)
        self.collabBasedList.setGeometry(QtCore.QRect(30, 460, 741, 101))
        self.collabBasedList.setFlow(QtWidgets.QListView.LeftToRight)
        self.collabBasedList.setObjectName("collabBasedList")
        self.populateContent(id)
        self.populateCollab(id)
        self.buyButton = QtWidgets  .QPushButton(self.centralwidget)
        self.buyButton.setObjectName(u"buyButton")
        self.buyButton.setGeometry(QtCore.QRect(310, 280, 75, 24))
        self.buyButton.clicked.connect(self.addToFav)
        self.buyButton.setText('Buy')
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "Go back"))
        #self.productLabel.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))

    def go_back(self):

        ui.setupUi(MainWindow)

    def addToFav(self):
        global user_favs
        id = self.id
        rating = 3
        name = df['product_name'][id]
        tupel = (name, id, rating)
        if tupel not in user_favs:
            user_favs.append(tupel)

    def populateContent(self, id):
        # (name, index)
        for name, ind in self.content_results:
            if ind == id:
                continue
            self.contentBasedList.addItem(QListWidgetItem(name))

    def populateCollab(self, id):
        for column in self.collab_results.columns:
            if column == 'productId':
                continue
            ind = int(column)
            if ind == id:
                continue
            self.collabBasedList.addItem(
                QListWidgetItem(df['product_name'][ind]))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
