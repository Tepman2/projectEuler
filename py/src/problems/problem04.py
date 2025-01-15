from utils.projectEulerProblem import ProjectEulerProblem
class Problem04(ProjectEulerProblem):
    description = """A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
    
    Find the largest palindrome made from the product of two 3-digit numbers."""
    def __init__(self):
        pass
        
    def solve(self) -> int:
        possible_answers = []
        for left in range(999, 100, -1):
            for right in range(999, 100, -1):
                product = left * right
                if self.isPalindrome(product):
                    possible_answers.append(product)

        possible_answers.sort()
        return possible_answers[-1]

            

    @staticmethod
    def isPalindrome(val):
        str_val = str(val)
        ret_val = False
        while len(str_val) > 1:
            if str_val[0] == str_val[-1]:
                str_val = str_val[1:-1]
            else:
                break
        else:
            ret_val = True
        return ret_val