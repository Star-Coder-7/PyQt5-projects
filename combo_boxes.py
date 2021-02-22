import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World!!!")

        self.setLayout(qtw.QVBoxLayout())

        myLabel = qtw.QLabel("Pick something from the list below: ")
        myLabel.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(myLabel)

        myCombo = qtw.QComboBox(self, editable=True, insertPolicy=qtw.QComboBox.InsertAtTop)

        myCombo.addItem("Pepperoni", "Something")
        myCombo.addItem("Cheese", 2)
        myCombo.addItem("Mushroom", qtw.QWidget)
        myCombo.addItem("Peppers")
        myCombo.addItems(["One", "Two", "Three"])
        myCombo.insertItem(2, "Third Thing")

        self.layout().addWidget(myCombo)

        myButton = qtw.QPushButton("Press Me!", clicked=lambda: pressIt())
        self.layout().addWidget(myButton)

        self.show()

        def pressIt():
            myLabel.setText(f"You picked {myCombo.currentText()}!")


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()

