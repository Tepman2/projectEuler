
#include "problem01.h"

unsigned long long ProjectEuler::Problem01::solve() {
    unsigned long long sum = 0;
    for( int i = 0; i < limit; i++ ) {
        if( i % 3 == 0 || i % 5 == 0 ) {
            sum += i;
        }
    }
    return( sum );
}
/*
int main() {
    using namespace ProjectEuler;
    Problem01 problem(1000);
    std::cout << "The answer is: " << problem.solve() << std::endl;
    return 0;
}
*/
