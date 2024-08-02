
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTreeView, QFileSystemModel

class FileExplorer(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(''))
        
        self.layout.addWidget(self.tree)
        self.setLayout(self.layout)
