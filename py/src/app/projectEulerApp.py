from PyQt5.QtWidgets import QGridLayout, QPushButton, QLCDNumber, QWidget, QVBoxLayout, QTextBrowser, QTabWidget
from utils.projectEulerTab import ProjectEulerTab

class ProjectEulerApp(QWidget):
    def __init__(self, problems):
        super().__init__()
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        tabWidget = QTabWidget(self)
        for num, problem in enumerate(problems, 1):
            tab = ProjectEulerTab(self, problem)
            tabWidget.addTab(tab, "Problem {:02n}".format(num))
        main_layout.addWidget(tabWidget)
        self.show()