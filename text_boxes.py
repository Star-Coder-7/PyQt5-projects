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

        myText = qtw.QTextEdit(self, lineWrapMode=qtw.QTextEdit.FixedColumnWidth, readOnly=False, plainText="TEXT!!!",
                               placeholderText='Hello World!', lineWrapColumnOrWidth=50, acceptRichText=True,
                               html='<h1><em><center>Big Header Text!</center></em></h1>')

        # myText.setFont(qtg.QFont('Arial', 18))

        self.layout().addWidget(myText)

        myButton = qtw.QPushButton("Press Me!", clicked=lambda: pressIt())

        self.layout().addWidget(myButton)

        self.show()

        def pressIt():
            myLabel.setText(f"You Typed {myText.toPlainText()}!")
            myText.setText('')


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
