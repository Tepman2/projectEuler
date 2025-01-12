#include <string>
namespace ProjectEuler {
    class Problem02 {
    private:
        unsigned long long max = 4000000;
        unsigned long long i;
        unsigned long long j;
    public:
        Problem02();
        unsigned long long solve();
        void next();
        unsigned long long num();
    };
}
