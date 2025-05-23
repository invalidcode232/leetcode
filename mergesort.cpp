#include <climits>
#include <print>
#include <vector>

using namespace std;

vector<int> merge(vector<int> v1, vector<int> v2) {
    int l1 = v1.size();
    int l2 = v2.size();

    vector<int> result;

    int i = 0, j = 0;

    while (i < l1 || j < l2) {
        int a = i < l1 ? v1[i] : INT_MAX;
        int b = j < l2 ? v2[j] : INT_MAX;

        if (a > b) {
            result.push_back(b);
            j++;
        }
        else{
            result.push_back(a);
            i++;
        }
    }

    return result;
}

vector<int> mergesort(vector<int> v) {
    if (v.size() == 1) {
        return v;
    }

    vector<int> v1(v.begin(), v.begin() + (v.size() / 2));
    vector<int> v2((v.begin() + v.size() / 2), v.end());

    return merge(mergesort(v1), mergesort(v2));
}

int main() {
    vector<int> v = {5, 2, 3, 6, 9, 1, 11};
    vector<int> v1 = {2, 5, 6};
    vector<int> v2 = {1, 3, 7};

    // auto v = merge(v1, v2);
    auto sv = mergesort(v);

    print("{}", sv);
}
