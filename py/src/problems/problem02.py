from utils.projectEulerProblem import ProjectEulerProblem
class Fibonacci:
    def __init__(self):
        self.first = 0
        self.second = 1

    def num(self):
        return self.second
    
    def next(self):
        tmp = self.first
        self.first = self.second
        self.second += tmp

class Problem02(ProjectEulerProblem):
    description = """Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""
    def __init__(self):
        self.limit = 4_000_000
    def solve(self) -> int:
        result = 0
        fibNum = Fibonacci()
        while fibNum.num() <= self.limit:
            if fibNum.num() % 2 == 0:
                result += fibNum.num()
            fibNum.next()
        return result