import math
from utils.projectEulerProblem import ProjectEulerProblem

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

class PrimeFactors:
    def __init__(self, num):
        self.num = num

    def find_prime_factors(self):
        factors = []
        if self.num % 2 == 0:
            factors.append(2)

        for i in range(3, math.isqrt(self.num), 2):
            if self.num % i == 0 and is_prime(i):
                factors.append(i)
        return factors

class Problem03(ProjectEulerProblem):
    description = """The prime factors of 13195 are 5, 7, 13, and 29.
    What is the largest prime factor of the number 600851475143?"""
    
    def solve(self) -> int:
        pf = PrimeFactors(600851475143)
        factors = pf.find_prime_factors()
        factors.sort()
        return factors[-1]