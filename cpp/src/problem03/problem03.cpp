#include <cmath>
#include <vector>
#include "problem03.h"
bool isPrime(unsigned long long val);
std::vector<unsigned long long> getPrimeFactors(unsigned long long val);
using namespace ProjectEuler;
unsigned long long Problem03::solve() {
    std::vector<unsigned long long> factors = getPrimeFactors(value);
    return factors.back();
}

std::vector<unsigned long long> getPrimeFactors(unsigned long long val) {
    unsigned long long tmp_val = val;
    std::vector<unsigned long long> ret_val;
    while(tmp_val % 2 == 0) {
        tmp_val /= 2;
        ret_val.push_back(2);
    }
    for(int i = 3; i < (int)std::sqrt(val); i += 2) {
        if(isPrime(i)) {
            while(tmp_val % i == 0) {
                ret_val.push_back(i);
                tmp_val /= i;
            }
        }

        if(tmp_val == 1) {
            break;
        }
    }
    return(ret_val);
}
bool isPrime(unsigned long long val) {
    for( int i = 2; i <= (int)std::sqrt(val); i++ ) {
        if( val % i == 0 ) {
            return false;
        }
    }
    return true;
}
