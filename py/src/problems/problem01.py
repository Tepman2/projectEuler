from utils.projectEulerProblem import ProjectEulerProblem
class Problem01(ProjectEulerProblem):
    description = """If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
        
        Find the sum of all of the multiples of 3 or 5 below 1000"""
    limit = 1000
    
    def __init__(self):
        pass
    
    def solve(self) -> int:
        result = 0
        for i in range(self.limit):
            if i % 3 == 0 or i % 5 == 0:
                result += i

        return result