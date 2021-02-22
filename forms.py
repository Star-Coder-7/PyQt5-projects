import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World!")

        formLayout = qtw.QFormLayout()
        self.setLayout(formLayout)

        label1 = qtw.QLabel("This is a Cool Label Row")
        label1.setFont(qtg.QFont("Arial", 24))

        fName = qtw.QLineEdit(self)
        lName = qtw.QLineEdit(self)

        formLayout.addRow(label1)
        formLayout.addRow("First Name", fName)
        formLayout.addRow("Last Name", lName)
        formLayout.addRow(qtw.QPushButton("Press Me!", clicked=lambda: pressIt()))

        self.show()

        def pressIt():
            label1.setText(f'You clicked the button, {fName.text()} {lName.text()}!')
            fName.setText('')
            lName.setText('')


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
