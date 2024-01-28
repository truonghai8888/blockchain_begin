import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget


class ButtonAndLabel(QWidget):
    def __init__(self):
        super(ButtonAndLabel, self).__init__()

        self.button = QPushButton("button")
        self.button.clicked.connect(self.buttonClicked)

        self.label = QLabel("label: before clicked")

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def buttonClicked(self):
        self.label.setText("label: after clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    button_and_label = ButtonAndLabel()
    button_and_label.show()
    sys.exit(app.exec_())
