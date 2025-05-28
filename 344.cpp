#include <vector>

using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {
        const auto n = s.size();

        if (n <= 1) return;

        for (int i = 0; i < n / 2; i++) {
            auto tmp = s[i];
            s[i] = s[n - i - 1];
            s[n - i - 1] = tmp;
        }
    }
};
