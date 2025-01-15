import math
def isPrime(num):
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