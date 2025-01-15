from utils import ProjectEulerProblem
from utils import primeFactors
class Problem05(ProjectEulerProblem):
    def __init__(self, limit=20):
        self.limit = limit
    description = """2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
    def solve(self)->int:
        factors = {}
        result = 1
        for i in range(2, self.limit + 1):
            i_factors = primeFactors(i)
            for num, iterations in i_factors.items():
                if num not in factors.keys():
                    factors[num] = iterations
                elif num in factors.keys():
                    factors[num] = max(factors[num], iterations)
        print(factors)
        for num, iterations in factors.items():
            result *= num ** iterations
        return result
    
if __name__ == '__main__':
    print(Problem05(10).solve())