from .primes import isPrime

def primeFactors(val):
    result = {}
    tmp_val = val
    idx = 2
    while tmp_val > 1:
        if isPrime(idx):
            while tmp_val % idx == 0:
                if idx not in result:
                    result[idx] = 1
                else:
                    result[idx] += 1
                tmp_val /= idx
        idx += 1
    return result


if __name__ == '__main__':
    print("Factors of 10: ", primeFactors(10))
    print("Factors of 20: ", primeFactors(20))
    print("Factors of 11: ", primeFactors(11))