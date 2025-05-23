#include <algorithm>
#include <string>

using namespace std;

class Solution {
public:
    string multiply(string num1, string num2) {
        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());

        int s1 = num1.size();
        int s2 = num2.size();
        int size_max = max(s1, s2);

        int i = 0;

        while (i < size_max) {

        }
    }
};
