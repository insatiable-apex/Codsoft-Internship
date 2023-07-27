from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(280, 345)
                MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
               
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.outputLabel = QtWidgets.QLabel(self.centralwidget)
                self.outputLabel.setGeometry(QtCore.QRect(10, 10, 261, 51))
                font = QtGui.QFont()
                font.setPointSize(22)
                font.setBold(False)
                font.setWeight(50)
                
                self.outputLabel.setFont(font)
                self.outputLabel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
                self.outputLabel.setMouseTracking(False)
                self.outputLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(53, 53, 53);\n"
        "border-radius:10px;")
                self.outputLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.outputLabel.setIndent(3)
                self.outputLabel.setObjectName("outputLabel")
                
                self.Cbutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("C"))
                self.Cbutton.setGeometry(QtCore.QRect(10, 70, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.Cbutton.setFont(font)
                self.Cbutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.Cbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);\n"
        "border-radius: 10px;")
                self.Cbutton.setDefault(False)
                self.Cbutton.setFlat(False)
                self.Cbutton.setObjectName("Cbutton")
                
                self.percentbutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("%"))
                self.percentbutton.setGeometry(QtCore.QRect(80, 70, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.percentbutton.setFont(font)
                self.percentbutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.percentbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);\n"
        "border-radius: 10px;\n"
        "")
                self.percentbutton.setDefault(False)
                self.percentbutton.setFlat(False)
                self.percentbutton.setObjectName("percentbutton")
                
                self.delbutton = QtWidgets.QPushButton(self.centralwidget,
                clicked=lambda:self.del_it())
                self.delbutton.setGeometry(QtCore.QRect(150, 70, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(12)
                self.delbutton.setFont(font)
                self.delbutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.delbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);\n"
        "border-radius: 10px;")
                self.delbutton.setDefault(False)
                self.delbutton.setFlat(False)
                self.delbutton.setObjectName("delbutton")
                
                self.divbutton = QtWidgets.QPushButton(self.centralwidget,
                clicked=lambda:self.press_it("/"))
                self.divbutton.setGeometry(QtCore.QRect(220, 70, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.divbutton.setFont(font)
                self.divbutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.divbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);\n"
        "border-radius: 10px;")
                self.divbutton.setDefault(False)
                self.divbutton.setFlat(False)
                self.divbutton.setObjectName("divbutton")
                
                self.sevenbutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("7"))
                self.sevenbutton.setGeometry(QtCore.QRect(10, 120, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.sevenbutton.setFont(font)
                self.sevenbutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.sevenbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 50, 50);\n"
        "border-radius: 10px;")
                self.sevenbutton.setDefault(False)
                self.sevenbutton.setFlat(False)
                self.sevenbutton.setObjectName("sevenbutton")
                
                self.eightbutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("8"))
                self.eightbutton.setGeometry(QtCore.QRect(80, 120, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.eightbutton.setFont(font)
                self.eightbutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.eightbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 50, 50);\n"
        "border-radius: 10px;")
                self.eightbutton.setDefault(False)
                self.eightbutton.setFlat(False)
                self.eightbutton.setObjectName("eightbutton")
               
                self.ninebutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("9"))
                self.ninebutton.setGeometry(QtCore.QRect(150, 120, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.ninebutton.setFont(font)
                self.ninebutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.ninebutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 50, 50);\n"
        "border-radius: 10px;\n"
        "")
                self.ninebutton.setDefault(False)
                self.ninebutton.setFlat(False)
                self.ninebutton.setObjectName("ninebutton")
                
                self.mulbutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("*"))
                self.mulbutton.setGeometry(QtCore.QRect(220, 120, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.mulbutton.setFont(font)
                self.mulbutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.mulbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);\n"
        "border-radius: 10px;")
                self.mulbutton.setDefault(False)
                self.mulbutton.setFlat(False)
                self.mulbutton.setObjectName("mulbutton")
                
                self.fourbutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("4"))
                self.fourbutton.setGeometry(QtCore.QRect(10, 170, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.fourbutton.setFont(font)
                self.fourbutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.fourbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 50, 50);\n"
        "border-radius: 10px;")
                self.fourbutton.setDefault(False)
                self.fourbutton.setFlat(False)
                self.fourbutton.setObjectName("fourbutton")
                
                self.fivebutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("5"))
                self.fivebutton.setGeometry(QtCore.QRect(80, 170, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.fivebutton.setFont(font)
                self.fivebutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.fivebutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 50, 50);\n"
        "border-radius: 10px;")
                self.fivebutton.setDefault(False)
                self.fivebutton.setFlat(False)
                self.fivebutton.setObjectName("fivebutton")
                
                self.sixbuttton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("6"))
                self.sixbuttton.setGeometry(QtCore.QRect(150, 170, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.sixbuttton.setFont(font)
                self.sixbuttton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.sixbuttton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 50, 50);\n"
        "border-radius: 10px;")
                self.sixbuttton.setDefault(False)
                self.sixbuttton.setFlat(False)
                self.sixbuttton.setObjectName("sixbuttton")
                
                self.subbutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("-"))
                self.subbutton.setGeometry(QtCore.QRect(220, 170, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.subbutton.setFont(font)
                self.subbutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.subbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);\n"
        "border-radius: 10px;\n"
        "")
                self.subbutton.setDefault(False)
                self.subbutton.setFlat(False)
                self.subbutton.setObjectName("subbutton")
                
                self.onebutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("1"))
                self.onebutton.setGeometry(QtCore.QRect(10, 220, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.onebutton.setFont(font)
                self.onebutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.onebutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 50, 50);\n"
        "border-radius: 10px;")
                self.onebutton.setDefault(False)
                self.onebutton.setFlat(False)
                self.onebutton.setObjectName("onebutton")
                
                self.twobutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("2"))
                self.twobutton.setGeometry(QtCore.QRect(80, 220, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.twobutton.setFont(font)
                self.twobutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.twobutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 50, 50);\n"
        "border-radius: 10px;")
                self.twobutton.setDefault(False)
                self.twobutton.setFlat(False)
                self.twobutton.setObjectName("twobutton")
                
                self.threebutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("3"))
                self.threebutton.setGeometry(QtCore.QRect(150, 220, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.threebutton.setFont(font)
                self.threebutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.threebutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 50, 50);\n"
        "border-radius: 10px;")
                self.threebutton.setDefault(False)
                self.threebutton.setFlat(False)
                self.threebutton.setObjectName("threebutton")
                
                self.addbutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("+"))
                self.addbutton.setGeometry(QtCore.QRect(220, 220, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.addbutton.setFont(font)
                self.addbutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.addbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(99, 99, 99);\n"
        "border-radius: 10px;")
                self.addbutton.setDefault(False)
                self.addbutton.setFlat(False)
                self.addbutton.setObjectName("addbutton")
                
                self.dzerobutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("00"))
                self.dzerobutton.setGeometry(QtCore.QRect(10, 270, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.dzerobutton.setFont(font)
                self.dzerobutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.dzerobutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 50, 50);\n"
        "border-radius: 10px;")
                self.dzerobutton.setDefault(False)
                self.dzerobutton.setFlat(False)
                self.dzerobutton.setObjectName("dzerobutton")
                
                self.zerobutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("0"))
                self.zerobutton.setGeometry(QtCore.QRect(80, 270, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                self.zerobutton.setFont(font)
                self.zerobutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.zerobutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 50, 50);\n"
        "border-radius: 10px;")
                self.zerobutton.setDefault(False)
                self.zerobutton.setFlat(False)
                self.zerobutton.setObjectName("zerobutton")
                
                self.decimalbutton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.deci_it())
                self.decimalbutton.setGeometry(QtCore.QRect(150, 270, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(14)
                font.setBold(False)
                font.setWeight(50)
                self.decimalbutton.setFont(font)
                self.decimalbutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.decimalbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(50, 50, 50);\n"
        "border-radius: 10px;")
                self.decimalbutton.setDefault(False)
                self.decimalbutton.setFlat(False)
                self.decimalbutton.setObjectName("decimalbutton")
                
                self.equalbutton = QtWidgets.QPushButton(self.centralwidget,
                clicked=lambda:self.compute_it())
                self.equalbutton.setGeometry(QtCore.QRect(220, 270, 51, 41))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.equalbutton.setFont(font)
                self.equalbutton.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
                self.equalbutton.setStyleSheet("background-color: rgb(255, 140, 0);\n"
        "color: rgb(255, 255, 255);\n"
        "border-radius: 10px;")
                self.equalbutton.setDefault(False)
                self.equalbutton.setFlat(False)
                self.equalbutton.setObjectName("equalbutton")
                self.percentbutton.raise_()
                self.Cbutton.raise_()
                self.outputLabel.raise_()
                self.delbutton.raise_()
                self.divbutton.raise_()
                self.sevenbutton.raise_()
                self.eightbutton.raise_()
                self.ninebutton.raise_()
                self.mulbutton.raise_()
                self.fourbutton.raise_()
                self.fivebutton.raise_()
                self.sixbuttton.raise_()
                self.subbutton.raise_()
                self.onebutton.raise_()
                self.twobutton.raise_()
                self.threebutton.raise_()
                self.addbutton.raise_()
                self.dzerobutton.raise_()
                self.zerobutton.raise_()
                self.decimalbutton.raise_()
                self.equalbutton.raise_()
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 280, 22))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
                self.outputLabel.setText(_translate("MainWindow", "0"))
                self.Cbutton.setText(_translate("MainWindow", "C"))
                self.percentbutton.setText(_translate("MainWindow", "%"))
                self.delbutton.setText(_translate("MainWindow", "Del"))
                self.divbutton.setText(_translate("MainWindow", "/"))
                self.sevenbutton.setText(_translate("MainWindow", "7"))
                self.eightbutton.setText(_translate("MainWindow", "8"))
                self.ninebutton.setText(_translate("MainWindow", "9"))
                self.mulbutton.setText(_translate("MainWindow", "X"))
                self.fourbutton.setText(_translate("MainWindow", "4"))
                self.fivebutton.setText(_translate("MainWindow", "5"))
                self.sixbuttton.setText(_translate("MainWindow", "6"))
                self.subbutton.setText(_translate("MainWindow", "-"))
                self.onebutton.setText(_translate("MainWindow", "1"))
                self.twobutton.setText(_translate("MainWindow", "2"))
                self.threebutton.setText(_translate("MainWindow", "3"))
                self.addbutton.setText(_translate("MainWindow", "+"))
                self.dzerobutton.setText(_translate("MainWindow", "00"))
                self.zerobutton.setText(_translate("MainWindow", "0"))
                self.decimalbutton.setText(_translate("MainWindow", "."))
                self.equalbutton.setText(_translate("MainWindow", "="))

        def press_it(self,pressed):
                if pressed=="C":
                       self.outputLabel.setText("0")       
                else:
                        if self.outputLabel.text() == "0":
                               self.outputLabel.setText("")
                        self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')

        def deci_it(self):
                sc = self.outputLabel.text()
                # if sc[-1] == sc:
                #       pass
                # else:
                #       self.outputLabel.setText(f'{sc}.')
                self.outputLabel.setText(f'{sc}.')

        def del_it(self):
                del_t = self.outputLabel.text()
                del_t = del_t[:-1]
                if len(del_t)==0:
                       self.outputLabel.setText("0")
                else:
                        self.outputLabel.setText(del_t)

        def compute_it(self):
               
                sc = self.outputLabel.text()
                if sc[-1]=="%":
                        sep = sc.split("*")
                        first = sep[0]
                        second = sep[1][:-1]

                        calculate = float(second)/100
                        ans = float(first)*calculate

                        check = str(ans)

                        fractional_part = check.split(".")[0]
                        if_no_zero_after = check.split(".")[1]

                        zeros = len(if_no_zero_after)
                        for i in if_no_zero_after:
                                if i =="0":
                                        zeros -=1 

                        if zeros == 0:
                                self.outputLabel.setText(fractional_part)
                        else:
                                self.outputLabel.setText(check)
                else:
                        try:
                                ans = eval(sc)

                                self.outputLabel.setText(str(ans))
                        except:
                                self.outputLabel.setText("Error press(C)")


        
                         
                      

               


if __name__ == "__main__":
    
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())
