from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Main Window")
        MainWindow.resize(361, 588)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("central widget")
        self.outputLabel = QtWidgets.QLabel(self.centralWidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.percentButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("C"))
        self.cButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.removeIt())
        self.arrowButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("/"))
        self.divideButton.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(275, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.nineButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.eightButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.minusButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("-"))
        self.minusButton.setGeometry(QtCore.QRect(275, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.sixButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.fourButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.addButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("+"))
        self.addButton.setGeometry(QtCore.QRect(275, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.threeButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.oneButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.twoButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.equalButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.mathIt())
        self.equalButton.setGeometry(QtCore.QRect(275, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.dotIt())
        self.decimalButton.setGeometry(QtCore.QRect(190, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.plusMinusButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.plusMinusIt())
        self.plusMinusButton.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusMinusButton.setFont(font)
        self.plusMinusButton.setObjectName("plusminusButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralWidget, clicked=lambda: self.pressIt("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 361, 21))
        self.menuBar.setObjectName("menu bar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("status bar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Remove character
    def removeIt(self):
        # Grab what's on the screen already
        screen = self.outputLabel.text()
        # Remove last item in list/string
        screen = screen[:-1]
        # Output back to the screen
        self.outputLabel.setText(screen)

    # Let's Do Some Math!
    def mathIt(self):
        # Grab what's on the screen already
        screen = self.outputLabel.text()
        try:
            # Do the math
            answer = eval(screen)
            # Output answer to the screen
            self.outputLabel.setText(str(answer))
        except:
            # Output error to the screen
            self.outputLabel.setText("ERROR")

    # Change from positive/negative
    def plusMinusIt(self):
        # Grab what's on the screen already
        screen = self.outputLabel.text()
        if "-" in screen:
            self.outputLabel.setText(screen.replace("-", ""))
        else:
            self.outputLabel.setText(f'-{screen}')

    # Add a decimal
    def dotIt(self):
        # Grab what's on the screen already
        screen = self.outputLabel.text()

        if screen[-1] == ".":
            pass
        else:
            self.outputLabel.setText(f'{screen}.')

    def pressIt(self, pressed):
        if pressed == "C":
            self.outputLabel.setText("0")
        else:
            # Check to see if starts with 0 and delete 0
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
                # Concatenate the pressed button with what was there already
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.plusMinusButton.setText(_translate("MainWindow", "+/-"))
        self.zeroButton.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
