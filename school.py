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
        self.b12.clicked.connect(self.save_student_details)

### Login Form ######

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
    #    self.fill_next_registration_number()

   # def fill_next_registration_number(self):
    #    try:
        ## Adding database connection ######## 
    #        rn = 0
    #        mydb = con.connect(host="localhost",user="root",password="",db="school")
    #        cursor = mydb.cursor()
    #        cursor.execute("select * from student")
    #        result = cursor.fetchall()
    #        if result:
    #            for stud in result:
    #                rn += 1
    #        self.tb11.setText(str(rn+1))
    #    except con.Error as e:
    #        print("Error occured in selected student reg number" + e)

    def save_student_details(self):
#        try:
        ## Adding database connection ########
#           mydb = con.connect(host="localhost",user="root",password="",db="school")
#            cursor = mydb.cursor()  
#            registration_number = self.tb11.text()
#            full_name = self.tb12.text()
#            gender = self.cb11.text()
#            date_of_birth = self.cb12.text()
#            Class = self.cb13.currentText()
#            address = self.mtb11.text()
#            parent_name = self.tb13.text()
#            email = self.tb14.text()
#            phone = self.tb15.text()

#            qry = "inset into student (registration_number,full_name,gender,date_of_birth,Class,address,parent_name,email,phone) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#            value = (registration_number,full_name,gender,date_of_birth,Class,address,parent_name,email,phone)
#            cursor.execute(qry,value)
#            mydb.commit()

            self.l12.setText("Saved Successfully :)")
            QMessageBox.information(self, "Registration Form", "Save Successfully! :)")
#        except con.Error as e:
#            self.l12.setText("Error in save student form" + e)

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()