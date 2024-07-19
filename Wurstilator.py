# import libraries, pyqt6
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import math

# calculator
class Wurstilator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wurstilator")

        # main layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # add text box
        self.textbox = QLineEdit()
        self.textbox.setReadOnly(True)
        self.layout.addWidget(self.textbox)

        # add grid layout for buttons
        self.button_layout = QGridLayout()
        self.layout.addLayout(self.button_layout)

        # button labels
        button_labels = [
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*', 'log',
            '1', '2', '3', '-', 'ln',
            '0', '.', '=', '+', 'clear'
        ]

        # create buttons and add to layout
        self.buttons = {}
        for i, label in enumerate(button_labels):
            button = QPushButton(label)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            self.button_layout.addWidget(button, i // 5, i % 5)
            self.buttons[label] = button

        # connect buttons
        for label, button in self.buttons.items():
            if label == '=':
                button.clicked.connect(self.evaluate_expression)
            elif label == 'clear':
                button.clicked.connect(self.clear_textbox)
            else:
                button.clicked.connect(lambda checked, text=label: self.textbox.setText(self.textbox.text() + text))

        self.show()
        self.textbox.setText("0")

    def evaluate_expression(self):
        try:
            expression = self.textbox.text()
            expression = expression.replace('sqrt', 'math.sqrt')
            expression = expression.replace('log', 'math.log10')
            expression = expression.replace('ln', 'math.log')
            result = eval(expression)
            self.textbox.setText(str(result))
        except Exception as e:
            self.textbox.setText("Error")

    def clear_textbox(self):
        self.textbox.setText("")

if __name__ == "__main__":
    app = QApplication([])
    window = Wurstilator()
    app.exec()
