#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, bool> isSeen;

        for (auto n : nums) {
            if (isSeen.find(n) != isSeen.end()) {
                isSeen[n] = true;
            }
            else {
                isSeen[n] = false;
            }
        }

        for (auto i: isSeen) {
            if (!i.second) return i.first;
        }

        return -1;
    }
};
