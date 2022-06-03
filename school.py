from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys
from PyQt6.uic import loadUiType
import mysql.connector as con

ui, _ = loadUiType('student.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.tabBar().setVisible(False)
        self.menubar.setVisible(False)
        self.bo1.clicked.connect(self.login)

        self.menu11.triggered.connect(self.show_add_new_student_tab)

    def login(self):
        un = self.tbo1.text()
        pw =self.tbo2.text()
        if(un =="admin" and pw =="admin"):
            self.menubar.setVisible(True)
            self.tabWidget.setCurrentIndex(1)
        else:
            QMessageBox.warning(self,"Login Form", "Invalid username and password, Try Again")
            self.l01.setText("Invalid username and password")

    ### Add new student   ###

    def show_add_new_student_tab(self):
        self.tabWidget.setCurrentIndex(2)
        self.fill_next_registration_number()

    def fill_next_registration_number(self):
        try:
            rn = 0
            mydb = con.connect(host="localhost",user="root",password="",db="school")
            cursor =mydb.cursor()
            cursor.execute("select * from student")
            result = cursor.fetchall()
            if result:
                for stud in result:
                    rn += 1
                self.tb11.setText(str(rn+1))
        except con.Error as e:
            print("Error occured in selected student reg number " + e)



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()