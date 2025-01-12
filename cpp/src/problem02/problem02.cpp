
#include "problem02.h"

ProjectEuler::Problem02::Problem02() {
    i = 0;
    j = 1;
}
void ProjectEuler::Problem02::next() {
    unsigned long long tmp = j;
    j += i;
    i = tmp;
}
unsigned long long  ProjectEuler::Problem02::num() {
    return j;
}
unsigned long long ProjectEuler::Problem02::solve() {
    int sum = 0;
    while( num() <= max ) {
        if( num() % 2 == 0 ) {
            sum += num();
        }
        next();
    }
    return sum;
}

/*
int main(int argc, char const *argv[])
{
    using namespace ProjectEuler;
    Problem02 fibNum = Problem02();
    std::cout << "The sum is: " << fibNum.solve() << std::endl;
    return 0;
}*/
