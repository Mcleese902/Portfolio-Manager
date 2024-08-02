
from PyQt6.Qsci import QsciScintilla, QsciLexerPython

class CodeEditor(QsciScintilla):
    def __init__(self):
        super().__init__()

        lexer = QsciLexerPython()
        self.setLexer(lexer)

        self.setUtf8(True)
        self.setMargins(0, 0, 3)
        self.setIndentationsUseTabs(True)
        self.setIndentationWidth(4)
