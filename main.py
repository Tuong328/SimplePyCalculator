import sys
from PyQt5.QtWidgets import *

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        string = ""
        textSpot = QLineEdit(string)

        # ROOT
        root = QVBoxLayout()
        root.addWidget(textSpot)

        # Buttons
        grid = QGridLayout()
        grid.setSpacing(10)

        buttonClear = QPushButton('C')

        def clear():
            textSpot.clear()

        buttonClear.clicked.connect(clear)

        def clickedSignToggle():
            if textSpot.text() != "":
                if (textSpot.text()[0] != '-'):
                    textSpot.setText("-" + textSpot.text())
                else:
                    positive = eval(textSpot.text()) * -1
                    textSpot.setText(str(positive))

        buttonNegativeToggle = QPushButton('+/-')
        buttonNegativeToggle.clicked.connect(clickedSignToggle)

        def clickedPercent():
            if textSpot.text() != "":
                numberPercented = int(textSpot.text()) / 100
                textSpot.setText(str(numberPercented))

        buttonPercent = QPushButton('%')
        buttonPercent.clicked.connect(clickedPercent)

        def clickedEquals():
            if textSpot.text() != "":
                equals = eval(textSpot.text())
                print(str(equals))
                textSpot.clear()
                textSpot.setText(str(equals))

        buttonEquals = QPushButton('=')
        buttonEquals.clicked.connect(clickedEquals)


        def clickedDivide():
            if textSpot.text() != "":
                textSpot.setText(textSpot.text() + buttonDivide.text())
        buttonDivide = QPushButton('/')
        buttonDivide.clicked.connect(clickedDivide)

        def clickedMultiply():
            if textSpot.text() != "":
                textSpot.setText(textSpot.text() + buttonMultiply.text())
        buttonMultiply = QPushButton('*')
        buttonMultiply.clicked.connect(clickedMultiply)

        def clickedAdd():
            if textSpot.text() != "":
                textSpot.setText(textSpot.text() + buttonAdd.text())
        buttonAdd = QPushButton('+')
        buttonAdd.clicked.connect(clickedAdd)

        def clickedSubtract():
            if textSpot.text() != "":
                textSpot.setText(textSpot.text() + buttonSubtract.text())
        buttonSubtract = QPushButton('-')
        buttonSubtract.clicked.connect(clickedSubtract)

        def clickedDecimal():
            textSpot.setText(textSpot.text() + buttonDecimal.text())
        buttonDecimal = QPushButton('.')
        buttonDecimal.clicked.connect(clickedDecimal)

        def clicked0():
            textSpot.setText(textSpot.text() + button0.text())
        button0 = QPushButton('0')
        button0.clicked.connect(clicked0)

        def clicked1():
            textSpot.setText(textSpot.text() + button1.text())
        button1 = QPushButton('1')
        button1.clicked.connect(clicked1)

        def clicked2():
            textSpot.setText(textSpot.text() + button2.text())
        button2 = QPushButton('2')
        button2.clicked.connect(clicked2)

        def clicked3():
            textSpot.setText(textSpot.text() + button3.text())
        button3 = QPushButton('3')
        button3.clicked.connect(clicked3)

        def clicked4():
            textSpot.setText(textSpot.text() + button4.text())
        button4 = QPushButton('4')
        button4.clicked.connect(clicked4)

        def clicked5():
            textSpot.setText(textSpot.text() + button5.text())
        button5 = QPushButton('5')
        button5.clicked.connect(clicked5)

        def clicked6():
            textSpot.setText(textSpot.text() + button6.text())
        button6 = QPushButton('6')
        button6.clicked.connect(clicked6)

        def clicked7():
            textSpot.setText(textSpot.text() + button7.text())
        button7 = QPushButton('7')
        button7.clicked.connect(clicked7)

        def clicked8():
            textSpot.setText(textSpot.text() + button8.text())
        button8 = QPushButton('8')
        button8.clicked.connect(clicked8)

        def clicked9():
            textSpot.setText(textSpot.text() + button9.text())
        button9 = QPushButton('9')
        button9.clicked.connect(clicked9)


        grid.addWidget(buttonClear, 0, 0)
        grid.addWidget(buttonNegativeToggle, 0, 1)
        grid.addWidget(buttonPercent, 0, 2)
        grid.addWidget(buttonDivide, 0, 3)
        grid.addWidget(button7, 1, 0)
        grid.addWidget(button8, 1, 1)
        grid.addWidget(button9, 1, 2)
        grid.addWidget(buttonMultiply, 1, 3)
        grid.addWidget(button4, 2, 0)
        grid.addWidget(button5, 2, 1)
        grid.addWidget(button6, 2, 2)
        grid.addWidget(buttonSubtract, 2, 3)
        grid.addWidget(button1, 3, 0)
        grid.addWidget(button2, 3, 1)
        grid.addWidget(button3, 3, 2)
        grid.addWidget(buttonAdd, 3, 3)
        grid.addWidget(button0, 4, 0)
        grid.addWidget(buttonDecimal, 4, 1)
        grid.addWidget(buttonEquals, 4, 3)

        root.addItem(grid)

        self.setLayout(root)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("JT's Python Calculator")
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
