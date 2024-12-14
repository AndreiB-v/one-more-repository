import sys
from os.path import isfile

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QSizePolicy, QSpacerItem, QPushButton, QWidget
from library import Ui_MainWindow
from card import Ui_Form
import sqlite3


class CardForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def place_info(self, info):
        self.show()
        self.setWindowTitle(info[0])
        self.nameText.setText(info[0])
        self.authorText.setText(info[1])
        self.yearText.setText(str(info[2]))
        self.genreText.setText(info[3])
        if isfile(f'pictures/{info[0]} {info[1].split(" ")[-1]}.png'):
            picture = QPixmap(f'pictures/{info[0]} {info[1].split(" ")[-1]}.png')
        else:
            picture = QPixmap('pictures/placeholder.png')
        self.pictureLabel.setPixmap(picture.scaled(170, 170))


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.setWindowTitle('Каталог библиотеки')
        self.cardForm = CardForm()
        self.findButton.clicked.connect(lambda x: self.update_list(self.find_results()))

    def clear_layout(self, layout):
        if 'Layout' in layout.__class__.__name__:
            while layout.count():
                child = layout.takeAt(0)
                self.clear_layout(child)
                if child.widget():
                    child.widget().deleteLater()

    def find_results(self):
        con = sqlite3.connect('bd/catalog.sqlite')
        cur = con.cursor()
        text = {'Автор': 'Authors.full_name', 'Название': 'Books.title'}[self.selectSort.currentText()]
        que = f'''SELECT Books.title, Authors.full_name, Books.year, Books.genre 
        FROM Authors
        INNER JOIN Books 
            ON Authors.id = Books.author
        WHERE {text} LIKE ?'''
        result = cur.execute(que, (f'%{self.sortBy.text()}%',)).fetchall()
        return result

    def update_list(self, books):
        self.allButtons = {}
        self.clear_layout(self.verticalLayout)
        for book in books:
            self.button = QPushButton(self.scrollAreaWidgetContents)
            self.button.setText(book[0])
            self.allButtons[book[0]] = [book[0], book[1], book[2], book[3]]
            self.button.clicked.connect(
                lambda state, btn=self.button: self.cardForm.place_info(self.allButtons[btn.text()]))
            self.verticalLayout.addWidget(self.button)
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.exit(app.exec())
