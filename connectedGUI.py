


from PyQt5 import QtCore, QtGui, QtWidgets
import authenticator
import requests
import pandas as pd
import json
import plotly.graph_objects as go
from datetime import datetime

class inputObject():
    def __init__(self, periodType, period, frequencyType, frequency, endDate, startDate, needExtendedHoursData):
        self.periodType = periodType
        self.period = period
        self.frequencyType = frequencyType
        self.frequency = frequency
        self.endDate = endDate
        self.startDate = startDate
        self.needExtendedHoursData = needExtendedHoursData


        #defualt values
        if self.period == '':
                if self.periodType == 'day':
                        self.period = '10'
                if self.periodType == 'month' or self.periodType == 'year' or self.periodType == 'ytd':
                        self.period = '1'
        if self.frequency == '':
                self.frequency = '1'
        

                
                



    def displayData(self):
        print("periodType: ", self.periodType)
        print("period: ", self.period)
        print("frequencyType: ", self.frequencyType)
        print("frequency: ", self.frequency)
        print("endDate: ", self.endDate)
        print("startDate: ", self.startDate)
        print("needExtendedHoursData: ", self.needExtendedHoursData)


        


        
            

        

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1417, 1067)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_7.addWidget(self.lineEdit)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_5)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_3.addWidget(self.line_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_9.addWidget(self.lineEdit_2)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_3.addWidget(self.line_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_10.addWidget(self.lineEdit_3)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_3.addWidget(self.line_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_3.addWidget(self.line_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1417, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #added code
        self.pushButton.clicked.connect(self.writePost)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "periodType"))
        self.comboBox.setItemText(0, _translate("MainWindow", "day"))
        self.comboBox.setItemText(1, _translate("MainWindow", "month"))
        self.comboBox.setItemText(2, _translate("MainWindow", "year"))
        self.comboBox.setItemText(3, _translate("MainWindow", "ytd"))
        self.label_2.setText(_translate("MainWindow", "The type of period to show. Valid values are day, month, year, or ytd (year to date). Default is day."))
        self.label_7.setText(_translate("MainWindow", "period"))
        self.label_8.setText(_translate("MainWindow", "The number of periods to show.\n"
"\n"
"Example: For a 2 day / 1 min chart, the values would be:\n"
"\n"
"period: 2\n"
"periodType: day\n"
"frequency: 1\n"
"frequencyType: min\n"
"\n"
"Valid periods by periodType (defaults marked with an asterisk):\n"
"\n"
"day: 1, 2, 3, 4, 5, 10*\n"
"month: 1*, 2, 3, 6\n"
"year: 1*, 2, 3, 5, 10, 15, 20\n"
"ytd: 1*"))
        self.label_9.setText(_translate("MainWindow", "frequencyType"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "minute"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "daily"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "weekly"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "monthly"))
        self.label_10.setText(_translate("MainWindow", "The type of frequency with which a new candle is formed.\n"
"\n"
"Valid frequencyTypes by periodType (defaults marked with an asterisk):\n"
"\n"
"day: minute*\n"
"month: daily, weekly*\n"
"year: daily, weekly, monthly*\n"
"ytd: daily, weekly*"))
        self.label_11.setText(_translate("MainWindow", "frequency"))
        self.label_12.setText(_translate("MainWindow", "The number of the frequencyType to be included in each candle.\n"
"\n"
"Valid frequencies by frequencyType (defaults marked with an asterisk):\n"
"\n"
"minute: 1*, 5, 10, 15, 30\n"
"daily: 1*\n"
"weekly: 1*\n"
"monthly: 1*"))
        self.label_14.setText(_translate("MainWindow", "endDate"))
        self.label_13.setText(_translate("MainWindow", "    \n"
"End date as milliseconds since epoch. If startDate and endDate are provided, period should not be provided. Default is previous trading day."))
        self.label_4.setText(_translate("MainWindow", "startDate"))
        self.label_3.setText(_translate("MainWindow", "Start date as milliseconds since epoch. If startDate and endDate are provided, period should not be provided."))
        self.label_5.setText(_translate("MainWindow", "needExtendedHoursData"))
        self.comboBox_2.setCurrentText(_translate("MainWindow", "True"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "False"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "True"))
        self.label_6.setText(_translate("MainWindow", "true to return extended hours data, false for regular market hours only. Default is true"))
        self.pushButton.setText(_translate("MainWindow", "Go!"))



    def writePost(self):
        newInput = inputObject(
            self.comboBox.currentText(),
            self.lineEdit.text(),
            self.comboBox_5.currentText(),
            self.lineEdit_2.text(),
            self.lineEdit_3.text(),
            self.lineEdit_4.text(),
            self.comboBox_2.currentText()
        )
        newInput.displayData()

        auth = authenticator.Authenticator()
        auth.generate_access_token()

        headers = {'Authorization': 'Bearer ' + auth.curr_access_token }
        resource_url = retrieve_price_history(newInput)
        response = requests.get(resource_url, headers=headers)
        
        print(response.status_code)
        json_response = response.json()
        # with open('data.json', 'w') as f:
        #         json.dump(json_response, f)
        df = pd.json_normalize(json_response['candles'])
        print(df)
        print(df.info())

        fig = go.Figure(data=[go.Candlestick(x=df['datetime'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

        fig.show()
        
        
        
def retrieve_price_history(inputObject):

    resource_url = "https://api.tdameritrade.com/v1/marketdata/AAPL/pricehistory"
    print("Welcome to TradeMaster200. Please enter a ticker symbol and data paramaters. (You may type in help at any time for a list of commands and defaults) ")
    
    resource_url += "?periodType=" + inputObject.periodType
    resource_url = resource_url + "&period=" + inputObject.period
    resource_url = resource_url + "&frequencyType=" + inputObject.frequencyType
    resource_url = resource_url + "&frequency=" + inputObject.frequency

    print(resource_url)
    return resource_url


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
