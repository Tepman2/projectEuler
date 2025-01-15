import sys
from PyQt5.QtWidgets import QApplication
from app import ProjectEulerApp
from problems import (Problem01, Problem02, Problem03, Problem04, Problem05, Problem06)

if __name__ == '__main__':
    problem_list = []

    problem_list.append(Problem01())
    problem_list.append(Problem02())
    problem_list.append(Problem03())
    problem_list.append(Problem04())
    problem_list.append(Problem05())
    problem_list.append(Problem06())
    app = QApplication(sys.argv)
    window = ProjectEulerApp(problem_list)
    sys.exit(app.exec_())