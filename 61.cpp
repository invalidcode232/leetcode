#include <print>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr) {
            return head;
        }

        ListNode* cur = head;

        // get size
        int n = 0;
        while (cur != nullptr) {
            n++;
            cur = cur->next;
        }

        if (n == 0 || k % n == 0) {
            return head;
        }

        int i = 0;
        ListNode* prev = nullptr;
        cur = head;

        while (cur->next != nullptr) {
            if (i == (n - (k % n))) {
                break;
            }

            i++;
            prev = cur;
            cur = cur->next;
        }

        ListNode* newHead = cur;
        ListNode* j = newHead;
        while (j->next != nullptr) {
            j = j->next;
        }

        prev->next = nullptr;
        j->next = head;

        return newHead;
    }
};
