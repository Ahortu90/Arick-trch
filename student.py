import imp
import PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
from PyQt6 import QtCore,QtWidgets
from PyQt6.uic import load_ui
from student_sqlite import Comunication

class Admin(QMainWindow):
    def __init__(self):
        super(Admin, self).__init__()
        load_ui('dash.ui', self)

        self.bt_menu.clicked.connect(self.move_menu)
        #class comunication sqlite
        self.all_students = Comunication()
        #self.Id = str()

        self.bt_register.hide()
        #bottons
        self.bt_refresh.clicked.connect(self.monstar_allstdents)
        self.