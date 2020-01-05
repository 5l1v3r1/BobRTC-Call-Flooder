from selenium import webdriver
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import selenium
import pause
from pynput.keyboard import Key, Controller

qtcreator_file  = "mainwindow.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sendCalls) 
        self.setFixedSize(self.size())     


    def sendCalls(self):        
        bob_url = self.lineEdit.text()
        time = self.lineEdit_2.text()
        call_amount = self.lineEdit_3.text()
        refresh = self.lineEdit_4.text()
        use_chrome = self.radioButton.isChecked() 
        use_firefox = self.radioButton_2.isChecked() 

        windows_user = os.getlogin()

        if use_chrome == True:
            options = webdriver.ChromeOptions() 
            options.add_argument(f"user-data-dir=C:\\Users\\{windows_user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default") 
            driver = webdriver.Chrome(options=options)   
        elif use_firefox == True: 
            driver = webdriver.Firefox()

        kb = Controller()                       

        def open_sites():
            try:
                driver.get('https://bobrtc.tel/')   
                radio_passed = True             
            except NameError:
                msg = QMessageBox()
                msg.setText("No Browser Has Been Selected.")
                msg.setStyleSheet("QLabel{ color: black}");
                msg.setWindowTitle("Error")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()  
                radio_pressed = False

            right_page = 'BobRTC' in driver.title

            if right_page == False:
                print('Error')
            else:
                print('WebPage Loaded Successfully')

            try:
                driver.find_element_by_id('loginButton')
            except selenium.common.exceptions.NoSuchElementException:
                pass

            while True:
                current_url = driver.current_url

                if 'bobrtc.live' in current_url:
                    break
                else:
                    pass
                    
            for i in range(int(call_amount)):   
                driver.execute_script(f"window.open('{bob_url}');")
                pause.seconds(int(time))

        while True:
            open_sites()
            pause.seconds(int(refresh))

            while len(driver.window_handles) > 1:
                kb.press(Key.ctrl)
                kb.press('w')
                kb.release('w')
                kb.release(Key.ctrl)
                pause.seconds(0.15)

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
