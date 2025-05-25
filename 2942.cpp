#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> result;
        int n = words.size();

        if (n == 0) {
            return result;
        }

        // int i = 0;
        for (int i = 0; i < n; i++) {
            string word = words[i];

            for (int j = 0; j < word.size(); j++) {
                if (word[j] == x) {
                    result.push_back(i);
                    break;
                }
            }
        }

        return result;
    }
};

int main() {
    Solution s;
    vector<string> words = {"abc","bcd","aaaa","cbc"};
    s.findWordsContaining(words, 'z');

    for (int i: s.findWordsContaining(words, 'a')) {
        cout << i << " ";
    }

    return 0;
}
