import sys
from PyQt5.QtWidgets import QApplication
from app.projectEulerApp import ProjectEulerApp
from problems.problem01 import Problem01
from problems.problem02 import Problem02
from problems.problem03 import Problem03

if __name__ == '__main__':
    problems = []
    problems.append(Problem01())
    problems.append(Problem02())
    problems.append(Problem03())
    app = QApplication(sys.argv)
    window = ProjectEulerApp(problems)
    sys.exit(app.exec_())