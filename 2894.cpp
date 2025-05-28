class Solution {
public:
    int differenceOfSums(int n, int m) {
        int tsum = n * (n + 1) / 2;
        int dsum = m * (n / m) * (n / m + 1);
        return tsum - dsum;
    }
};
