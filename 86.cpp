#include <print>
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* smallHead = nullptr;
        ListNode* smallTail = nullptr;
        ListNode* largeHead = nullptr;
        ListNode* largeTail = nullptr;

        ListNode* cur = head;

        while (cur != nullptr) {
            if (cur->val >= x) {
                if (largeHead == nullptr) {
                    largeHead = cur;
                    largeTail = largeHead;
                }
                else {
                    largeTail->next = cur;
                    largeTail = largeTail->next;
                }
            }
            else {
                if (smallHead == nullptr) {
                    smallHead = cur;
                    smallTail = smallHead;
                }
                else {
                    smallTail->next = cur;
                    smallTail = smallTail->next;
                }
            }

            cur = cur->next;
        }

        if (largeTail != nullptr) {
            largeTail->next = nullptr;
        }

        if (smallHead == nullptr) {
            return largeHead;
        }

        smallTail->next = largeHead;

        // ListNode* i = smallHead;

        // while(i != nullptr) {
        //     std::print("{} ", i->val);
        //     i = i->next;
        // }

        return smallHead;
    }
};

void addNode(ListNode*& head, int val) {
    ListNode* newNode = new ListNode;
    newNode->val = val;
    newNode->next = nullptr;

    if (head == nullptr) {
        head = newNode;
        return;
    }

    ListNode* cur = head;

    while (cur->next != nullptr) {
        cur = cur->next;
    }

    cur->next = newNode;
}

int main() {
    Solution s;

    ListNode* head = nullptr;
    addNode(head, 1);
    addNode(head, 4);
    addNode(head, 3);
    addNode(head, 2);
    addNode(head, 5);
    addNode(head, 2);


    auto newHead = s.partition(head, 3);

    // ListNode* i = newHead;
    // while (i != nullptr) {
    //     std::print("{} ", i->val);

    //     i = i->next;
    // }

    return 0;
}
