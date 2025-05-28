#include <algorithm>
#include <print>
#include <string>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        string fs = "";
        transform(s.begin(), s.end(), s.begin(),
                  ::tolower);

        for (auto c : s) {
            if (c >= '0' && c <= '9' || c >= 'a' && c <= 'z') {
                fs+= c;
            }
        }

        // print("{}", fs);
        auto ln = fs.size();
        if (ln == 1) {
            return true;
        }

        for (int i = 0; i < ln / 2; i++) {
            if (fs[i] != fs[ln - i - 1]) {
                return false;
            }
        }

        return true;
    }
};

int main() {
    Solution s;
    print("{}", s.isPalindrome("0P"));
}
