from utils import ProjectEulerProblem

class Problem06(ProjectEulerProblem):
    description = """The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 +...+ 10^2 = 385.
    The square of the sum of the first ten natural numbers is,
    (1 + 2 +...+10)^2 = 55^2 = 3025.
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
    
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""
    
    def __init__(self, limit=100):
        self.limit = limit
    
    def solve(self) -> int:
        sum_of_squares = 0
        square_of_sum = sum(range(self.limit + 1))
        for i in range(1, self.limit + 1):
            sum_of_squares += i ** 2

        square_of_sum = square_of_sum ** 2
        return square_of_sum - sum_of_squares