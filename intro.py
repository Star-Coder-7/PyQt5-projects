import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World!!!")

        self.setLayout(qtw.QVBoxLayout())

        myLabel = qtw.QLabel("Hello World!! What's your name?")

        myLabel.setFont(qtg.QFont('Arial', 18))

        self.layout().addWidget(myLabel)

        myEntry = qtw.QLineEdit()
        myEntry.setObjectName("Name Field")
        myEntry.setText("")

        self.layout().addWidget(myEntry)

        myButton = qtw.QPushButton("Press Me!", clicked=lambda: pressIt())

        self.layout().addWidget(myButton)

        self.show()

        def pressIt():
            myLabel.setText(f"Hello {myEntry.text()}")


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()

