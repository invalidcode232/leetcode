#include <string>
#include <map>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> m;
        map<char, int> n;

        for (const auto c: s) {
            if (!m.contains(c)) {
                m[c] = 1;
            }
            else {
                m[c]++;
            }
        }

        for (const auto c: t) {
            if (!m.contains(c)) return false;

            if (!n.contains(c)) {
                n[c] = 1;
            }
            else {
                n[c]++;
            }
        }

        return m == n;
    }
};
