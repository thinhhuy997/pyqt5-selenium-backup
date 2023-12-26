# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tds2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtCore import QFile, QTextStream


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 605)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 10, 741, 80))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.addAccountButton = QtWidgets.QPushButton(self.frame)
        self.addAccountButton.setGeometry(QtCore.QRect(20, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.addAccountButton.setFont(font)
        self.addAccountButton.setObjectName("addAccountButton")
        self.addProxyButton = QtWidgets.QPushButton(self.frame)
        self.addProxyButton.setGeometry(QtCore.QRect(130, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.addProxyButton.setFont(font)
        self.addProxyButton.setObjectName("addProxyButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 130, 1001, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        # self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 90, 741, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1064, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # new
        self.addAccountButton.clicked.connect(self.add_accounts_from_file)
        self.addProxyButton.clicked.connect(self.add_proxies_from_file)

        self.accounts = []

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addAccountButton.setText(_translate("MainWindow", "Add accounts"))
        self.addProxyButton.setText(_translate("MainWindow", "Add proxies"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "tds_username"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "tds_pass"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "face_uid"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "face_pass"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "cookie"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "token"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "proxy"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "user_agent"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "status"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "action"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        self.label.setText(_translate("MainWindow", "File:"))

    def add_row(self, row_index, data):
        _translate = QtCore.QCoreApplication.translate
        for column_index, (key, value) in enumerate(data.items()):
            item = QtWidgets.QTableWidgetItem()
            item.setText(_translate("MainWindow", str(value)))
            self.tableWidget.setItem(row_index, column_index, item)

    def add_accounts_to_table(self, accounts):
        self.tableWidget.setRowCount(len(accounts))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        for row_index, account_data in enumerate(accounts):
            self.add_row(row_index, account_data)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    def add_accounts_from_file(self):
        # Open file Dialog
        file_name, _ = QFileDialog.getOpenFileName(None, "Open File", "", "All Files (*);;Text Files (*.txt)")
        
        # Read file and import to data table
        if file_name:
            self.label.setText(str(file_name))

            file = QFile(file_name)

            if file.open(QFile.ReadOnly | QFile.Text):
                stream = QTextStream(file)
                facebook_accounts_content = stream.readAll()
                # remove first and last space
                facebook_accounts_content = facebook_accounts_content.strip()

                account_lines = facebook_accounts_content.split('\n')

                accounts = self.file_preprocessing(account_lines)

                # Add data to the data table
                self.add_accounts_to_table(accounts)
                
                file.close()
            else:
                print(f"Error opening file: {file.errorString()}")

    def file_preprocessing(self, account_lines: list):
        self.accounts = []
        for account_line in account_lines:
            account_values = account_line.split('|')
            account_obj = {
                "tds_username": account_values[0], 
                "tds_pass": account_values[1], 
                "face_uid": account_values[2], 
                "face_pass": account_values[3],
                "cookie": account_values[5]
                }
            self.accounts.append(account_obj)
        return self.accounts
    
    def add_proxies_from_file(self, accounts):
    
        if self.tableWidget.rowCount() == 0:
            print("You must add accounts first")
        else:
            # Open file Dialog
            file_name, _ = QFileDialog.getOpenFileName(None, "Open File", "", "All Files (*);;Text Files (*.txt)")
                
            # Read file and import to data table
            if file_name:
                self.label.setText(str(file_name))

                file = QFile(file_name)

                if file.open(QFile.ReadOnly | QFile.Text):
                    stream = QTextStream(file)
                    proxies_content = stream.readAll()
                    # remove first and last space
                    proxies_content = proxies_content.strip()

                    proxies_lines = proxies_content.split('\n')

                    # Add proxies to the accounts
                    
                    count = 0
                    for account in self.accounts:
                        if count == len(proxies_lines):
                            # reset count to 0
                            count = 0

                        account["proxy"] = proxies_lines[count]
                        
                        # increase count
                        count += 1
                        

                    for account in self.accounts:
                        print(account)
                        break

                    file.close()
                else:
                    print(f"Error opening file: {file.errorString()}")
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
