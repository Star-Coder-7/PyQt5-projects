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

        mySpin = qtw.QSpinBox(self, value=10, maximum=100, minimum=0, singleStep=5, prefix='#', suffix='!!!',)

        mySpin.setFont(qtg.QFont('Arial', 18))

        self.layout().addWidget(mySpin)

        myButton = qtw.QPushButton("Press Me!", clicked=lambda: pressIt())

        self.layout().addWidget(myButton)

        self.show()

        def pressIt():
            myLabel.setText(f"You picked {mySpin.value()}!")


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
