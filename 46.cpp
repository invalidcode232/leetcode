#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;

        if (nums.size() == 0) {
            return {{}};
        }

        auto splice = vector<int>(nums.begin() + 1, nums.end());
        auto prev_perms = permute(splice);

        for (const auto p: prev_perms) {
            for (int i = 0; i < p.size() + 1; i++) {
                auto cur_p = p;
                cur_p.insert(cur_p.begin() + i, nums[0]);

                res.push_back(cur_p);
            }
        }

        return res;
    }
};
