import sys
from functools import partial
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

def greet(name):

    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText (f"hello, {name}")

    
app = QApplication([])
window = QWidget()
window.setWindowTitle("signals and slots")
layout = QVBoxLayout()

button = QPushButton("greet")
button.clicked.connect(partial(greet, "cemre"))

layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)

window.setLayout(layout)
window.show()

sys.exit(app.exec())








