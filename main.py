import datetime
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal
import time
import Analysis_Logic
import timer
from ui import Ui_MainWindow
import Suggestion_Generator
import Postgresql
# import RasberryPY_SystemLogic




class DataBaseThread(QtCore.QObject):
    log = ""
    password = ""
    postgre = Postgresql.PostgreS
    Isconnect = QtCore.pyqtSignal(bool)
    Isautorization = QtCore.pyqtSignal(bool)
    resultText = ""
    endTime = time.time()
    startTime = time.time()

    def connected(self):
        self.Isconnect.emit(False)
        # if self.postgre.connect(self=self.postgre):
        #     self.Isconnect.emit(False)
        #     print("connect")
        # else:
        #     self.Isconnect.emit(True)


    def authorization(self):
        if self.postgre.authorization(self=self.postgre, login=self.log, password=self.password):
            self.Isautorization.emit(True)
            # print(self.log)
        else:
            self.Isautorization.emit(False)
        # if self.log == "admin" and self.password == "admin":
        #     self.Isautorization.emit(True)
        # else:
        #     self.Isautorization.emit(False)


    def send(self):
        print("ff")
        self.postgre.commit(self=self.postgre, result=self.resultText, startTime=self.startTime, endTime=self.endTime)

class External(QThread):
    word = {}
    countChanged = pyqtSignal(str)
    result = ""
    selfUI = object
    connect = pyqtSignal(bool)
    password = ""
    email = ""

    def run(self):
        timer.start(self.countChanged)
        self.result = Analysis_Logic.Step_One(self.word, self.countChanged)
        if self.result == '' or self.result == 'Error':
            self.selfUI.error()
        else:
            self.selfUI.result_widget(self.result)



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.result = ""
        self.startTime = datetime.datetime.today()
        self.endTime = datetime.datetime.today()
        self.email = ""
        self.password = ""
        self.calc = External()
        self.calc.selfUI = self
        self.thread = QtCore.QThread()
        self.database = DataBaseThread()
        self.database.moveToThread(self.thread)
        self.database.Isconnect.connect(self.onConnected)
        self.thread.started.connect(self.database.connected)
        self.database.Isautorization.connect(self.goStep)
        # self.rassbery = RasberryPY_SystemLogic.Rasberry
        self.thread.start()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Voice Analyzer')
        self.setFixedSize(470,600)
        self.ui.widget_2.close()
        self.ui.widget_3.close()
        self.ui.widget.show()
        self.ui.buttonSingIn.clicked.connect(self.autorization)
        self.ui.buttonRun.clicked.connect(self.run)
        self.ui.buttonBackW1.clicked.connect(self.back)
        self.ui.buttonBackW2.clicked.connect(self.back)
        self.ui.buttonReplay.clicked.connect(self.replay)
        self.ui.buttonSendResult.clicked.connect(self.send)
        self.ui.buttonReconnected.setVisible(False)

    def autorization(self):
        self.email = self.ui.emailEdit.text()
        self.password = self.ui.passwordEdit.text()
        self.database.log = self.email
        self.database.password = self.password
        self.thread.childEvent(self.database.authorization())


    def goStep(self,isaur):
        if isaur:
            self.ui.widget.close()
            self.ui.widget_2.show()
            self.ui.labelError.setText("")
        else:
            self.ui.labelError.setText("Incorrect login or password")

    def error(self):
        self.ui.TimeEdit.setText('Error')

    def connect(self):

        self.thread.start()

    def reconnect(self):
        self.thread.childEvent(self.connect())

    def run(self):

        word = Suggestion_Generator.wheel_rotation_random()
        self.ui.WordEdit.setText(f"{word[0]} {word[1]} {word[2]}")

        # self.rassbery.onPin(word[3],word[4],word[5])
        self.startTime = datetime.datetime.today()
        self.calc.word = word
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.selfUI = self
        self.calc.start()

    def send(self):
        self.database.resultText = self.result
        self.database.startTime = self.startTime
        self.database.endTime = self.endTime
        self.thread.childEvent(self.database.send())

    def onCountChanged(self, value):
        self.ui.TimeEdit.setText(value)

    def onConnected(self, value):
        self.ui.buttonReconnected.setVisible(value)

    def result_widget(self, result):

        self.ui.widget_2.close()
        self.ui.widget_3.show()
        self.rassbery.offPin()
        self.result = result
        self.endTime = datetime.datetime.today()
        self.ui.plainTextResult.setPlainText(result)
        self.ui.time.setText(str(self.endTime.strftime("%M.%S")))

    def back(self):
        self.ui.widget_2.close()
        self.ui.widget_3.close()
        self.ui.widget.show()
        self.ui.WordEdit.setText("")

    def replay(self):
        self.ui.widget_3.close()
        self.ui.widget_2.show()
        self.ui.WordEdit.setText("")



app = QtWidgets.QApplication([])
application = Window()
application.show()

sys.exit(app.exec_())