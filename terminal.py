
from PyQt6.QtWidgets import QPlainTextEdit

class Terminal(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        self.setReadOnly(True)
        self.appendPlainText("Terminal ready...")
