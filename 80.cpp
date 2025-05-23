#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();

        int i = 1;
        int count = 1;
        int last = nums[0];

        while (i < n) {
            int cur = nums[i];
            if (cur == last) {
                count++;
            }
            else {
                count = 1;
            }

            int rem_l = -1, rem_r = -1;
            if (count > 2) {
                rem_l = i;
                rem_r = i;

                while (rem_r < n) {
                    if (nums[rem_r] != cur) {
                        break;
                    }

                    rem_r++;
                }

                nums.erase(nums.begin() + rem_l, nums.begin() + rem_r);
                n = nums.size();
                count = 1;
            }

            last = nums[i];
            i++;
        }

        return n;
    }
};

int main() {
    Solution s;
    vector<int> vec = {0,0,1,1,1,1,2,3,3};
    cout << s.removeDuplicates(vec);
}
