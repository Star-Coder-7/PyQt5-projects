import sys
import os
import docx2txt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *


class MainApp(QMainWindow):

    def __init__(self):
        super().__init__()

        # window title
        self.title = "Google Doc Clone"
        self.setWindowTitle(self.title)

        # editor section
        self.editor = QTextEdit(self)
        self.setCentralWidget(self.editor)

        # create menu bar and toolbar first
        self.createMenuBar()
        self.createToolbar()

        # after creating tool bar we can call and select font size
        font = QFont('Times', 12)
        self.editor.setFont(font)
        self.editor.setFontPointSize(12)

        # stores path
        self.path = ''

    def createMenuBar(self):
        menuBar = QMenuBar(self)

        """ add elements to the menu bar """
        # App icon will go here
        app_icon = menuBar.addMenu(QIcon("doc_icon.png"), "icon")

        # file menu **
        fileMenu = QMenu("File", self)
        menuBar.addMenu(fileMenu)

        saveAction = QAction('Save', self)
        saveAction.triggered.connect(self.fileSave)
        fileMenu.addAction(saveAction)

        openAction = QAction('Open', self)
        openAction.triggered.connect(self.fileOpen)
        fileMenu.addAction(openAction)

        renameAction = QAction('Rename', self)
        renameAction.triggered.connect(self.fileSaveAs)
        fileMenu.addAction(renameAction)

        pdfAction = QAction("Save as PDF", self)
        pdfAction.triggered.connect(self.savePdf)
        fileMenu.addAction(pdfAction)

        # edit menu **
        editMenu = QMenu("Edit", self)
        menuBar.addMenu(editMenu)

        # paste
        pasteAction = QAction('Paste', self)
        pasteAction.triggered.connect(self.editor.paste)
        editMenu.addAction(pasteAction)

        # clear
        clearAction = QAction('Clear', self)
        clearAction.triggered.connect(self.editor.clear)
        editMenu.addAction(clearAction)

        # select all
        selectAction = QAction('Select All', self)
        selectAction.triggered.connect(self.editor.selectAll)
        editMenu.addAction(selectAction)

        # view menu **
        viewMenu = QMenu("View", self)
        menuBar.addMenu(viewMenu)

        # fullscreen
        fullscreenAction = QAction('Full Screen View', self)
        fullscreenAction.triggered.connect(lambda: self.showFullScreen())
        viewMenu.addAction(fullscreenAction)

        # normal screen
        normalScreenAction = QAction('Normal View', self)
        normalScreenAction.triggered.connect(lambda: self.showNormal())
        viewMenu.addAction(normalScreenAction)

        # minimize
        minScreenAction = QAction('Minimize', self)
        minScreenAction.triggered.connect(lambda: self.showMinimized())
        viewMenu.addAction(minScreenAction)

        self.setMenuBar(menuBar)

    def createToolbar(self):
        # Using a title
        ToolBar = QToolBar("Tools", self)

        # undo
        undoAction = QAction(QIcon(os.path.join("img", "undo.png")), 'Undo', self)
        undoAction.triggered.connect(self.editor.undo)
        ToolBar.addAction(undoAction)

        # redo
        redoAction = QAction(QIcon(os.path.join("img", "redo.png")), 'Redo', self)
        redoAction.triggered.connect(self.editor.redo)
        ToolBar.addAction(redoAction)

        # adding separator
        ToolBar.addSeparator()

        # copy
        copyAction = QAction(QIcon(os.path.join("img", "copy.png")), 'Copy', self)
        copyAction.triggered.connect(self.editor.copy)
        ToolBar.addAction(copyAction)

        # cut
        cutAction = QAction(QIcon(os.path.join("img", "cut.png")), 'Cut', self)
        cutAction.triggered.connect(self.editor.cut)
        ToolBar.addAction(cutAction)

        # paste
        pasteAction = QAction(QIcon(os.path.join("img", "paste.png")), 'Paste', self)
        pasteAction.triggered.connect(self.editor.paste)
        ToolBar.addAction(pasteAction)

        # adding separator
        ToolBar.addSeparator()
        ToolBar.addSeparator()

        # fonts
        self.fontCombo = QComboBox(self)
        self.fontCombo.addItems(["Courier Std", "Hellentic Typewriter Regular", "Helvetica", "Arial", "SansSerif",
                                 "Helvetica", "Times", "Monospace"])
        self.fontCombo.activated.connect(self.set_font)  # connect with function
        ToolBar.addWidget(self.fontCombo)

        # font size
        self.fontSize = QSpinBox(self)
        self.fontSize.setValue(12)
        self.fontSize.valueChanged.connect(self.setFontSize)  # connect with function
        ToolBar.addWidget(self.fontSize)

        # separator
        ToolBar.addSeparator()

        # bold
        boldAction = QAction(QIcon(os.path.join("img", "bold.png")), 'Bold', self)
        boldAction.triggered.connect(self.boldText)
        ToolBar.addAction(boldAction)

        # underline
        underlineAction = QAction(QIcon(os.path.join("img", "underline.png")), 'Underline', self)
        underlineAction.triggered.connect(self.underlineText)
        ToolBar.addAction(underlineAction)

        # italic
        italicsAction = QAction(QIcon(os.path.join("img", "italics.png")), 'Italic', self)
        italicsAction.triggered.connect(self.italicText)
        ToolBar.addAction(italicsAction)

        # separator
        ToolBar.addSeparator()

        # text alignment
        rightAlignmentAction = QAction(QIcon(os.path.join("img", "right_align.png")), 'Align Right', self)
        rightAlignmentAction.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignRight))
        ToolBar.addAction(rightAlignmentAction)

        leftAlignmentAction = QAction(QIcon(os.path.join("img", "left_align.png")), 'Align Left', self)
        leftAlignmentAction.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignLeft))
        ToolBar.addAction(leftAlignmentAction)

        justificationAction = QAction(QIcon(os.path.join("img", "justification.png")), 'Center/Justify', self)
        justificationAction.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignCenter))
        ToolBar.addAction(justificationAction)

        # separator
        ToolBar.addSeparator()

        # zoom in
        zoomInAction = QAction(QIcon(os.path.join("img", "zoom_in.png")), 'Zoom in', self)
        zoomInAction.triggered.connect(self.editor.zoomIn)
        ToolBar.addAction(zoomInAction)

        # zoom out
        zoomOutAction = QAction(QIcon(os.path.join("img", "zoom_out.png")), 'Zoom out', self)
        zoomOutAction.triggered.connect(self.editor.zoomOut)
        ToolBar.addAction(zoomOutAction)

        # separator
        ToolBar.addSeparator()

        self.addToolBar(ToolBar)

    def italicText(self):
        # if already italic, change into normal, else italic
        state = self.editor.fontItalic()
        self.editor.setFontItalic(not state)

    def underlineText(self):
        # if already underlined, change into normal, else underlined
        state = self.editor.fontUnderline()
        self.editor.setFontUnderline(not state)

    def boldText(self):
        # if already bold, make normal, else make bold
        if self.editor.fontWeight() != QFont.Bold:
            self.editor.setFontWeight(QFont.Bold)
            return
        self.editor.setFontWeight(QFont.Normal)

    def set_font(self):  # function name is set_font because setFont is a pyqt5 method
        font = self.fontCombo.currentText()
        self.editor.setCurrentFont(QFont(font))

    def setFontSize(self):
        value = self.fontSize.value()
        self.editor.setFontPointSize(value)

        # we can also make it one liner without writing such function.
        # by using lambda function -
        # self.fontSize.valueChanged.connect(self.editor.setFontPointSize(self.fontSize.value()))

    def fileOpen(self):
        self.path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.text);Text documents ("
                                                                          "*.txt);""All files (*.*)")

        try:
            text = docx2txt.process(self.path)  # docx2txt
            # with open(self.path, 'r') as f:
            #     text = f.read()
            # doc = Document(self.path)         # if using docx
            # text = ''
            # for line in doc.paragraphs:
            #     text += line.text
        except Exception as e:
            print(e)
        else:
            self.editor.setText(text)
            self.updateTitle()

    def fileSave(self):
        print(self.path)
        if self.path == '':
            # If we do not have a path, we need to use Save As.
            self.fileSaveAs()

        text = self.editor.toPlainText()

        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.updateTitle()
        except Exception as e:
            print(e)

    def fileSaveAs(self):
        self.path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "text documents (*.text);Text documents ("
                                                                          "*.txt);All files (*.*)")

        if self.path == '':
            return  # If dialog is cancelled, will return ''

        text = self.editor.toPlainText()

        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.updateTitle()
        except Exception as e:
            print(e)

    def updateTitle(self):
        self.setWindowTitle(self.title + ' ' + self.path)

    def savePdf(self):
        f_name, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf);;All files()")
        print(f_name)

        if f_name != '':  # if name not empty
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(f_name)
            self.editor.document().print_(printer)


app = QApplication(sys.argv)
window = MainApp()
window.show()
sys.exit(app.exec_())
