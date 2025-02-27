from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel, QMessageBox
from project import HRWF, projectMasterList
class GUI:
    def __init__(self, instanceUrl, username, password):
        self.app = QApplication([])
        self.app.setStyle('Fusion')
        self.app.setStyleSheet("QWidget { margin: 5ex; }")
        self.hrwf = HRWF(instanceUrl,  username, password)
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Select Project"))


        for x in projectMasterList:
            button = QPushButton(x)
            button.clicked.connect(self.__mainProjectView)
            self.layout.addWidget(button)
            
        self.window.setLayout(self.layout)
        self.window.show()

        
    def exec(self):
        self.app.exec()
    
    def __mainProjectView(self):
        self.projectLayout = QVBoxLayout()
        self.projectLayout.addWidget(QLabel("Test"))
        self.window.setLayout(self.projectLayout)
        self.window.show()