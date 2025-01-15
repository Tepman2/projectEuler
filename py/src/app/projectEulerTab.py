from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextBrowser, QLCDNumber, QPushButton

class ProjectEulerTab(QWidget):
    def __init__(self, parent, problem ):
        super().__init__(parent)
        self.problem = problem
        self.alignment = QVBoxLayout()
        self.setLayout(self.alignment)
        self.desc = QTextBrowser()
        self.desc.setText(problem.description)
        self.alignment.addWidget(self.desc)
        self.display = QLCDNumber()
        self.button = QPushButton()
        self.button.setText("Solve")                
        self.button.clicked.connect(self.on_button_clicked)
        self.alignment.addWidget(self.button)
        self.alignment.addWidget(self.display)

    def on_button_clicked(self):
        result = self.problem.solve()
        self.display.setDigitCount(len(str(result)))
        self.display.display(result)
        self.display.update()
