#include <iostream>

double binpow(double a, double b) {
    double result = 1;
    while (b > 0) {
        if ((long long) b % 2 == 1) result *= a;
        a *= a;
        b /= 2;
    }

    return result;
}

class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0 || x == 1) { // Check for edge cases
            return 1.0;
        }

        double res = binpow(x, abs(n));

        if (n < 0) {
            res = 1 / res;
        }

        return res;
    }
};

int main() {

    Solution s;
    double result = s.myPow(2.1, 3);
    std::cout << result << std::endl;
}
