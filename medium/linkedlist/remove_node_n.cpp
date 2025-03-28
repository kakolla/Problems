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



 class Solution {
    public:
        ListNode* removeNthFromEnd(ListNode* head, int n) {
            if (head == nullptr) return nullptr;

            // can solve in one pass with greedy
            // approach (2 ptrs )
            ListNode* first = head;
            for (int i = 0; i < n; ++i) {
                first = first->next;
            }

            if (first == nullptr) {
                // edge case: delete first elem
                if (head->next == nullptr) {
                    return nullptr;
                } else {
                    head = head->next;
                    return head;
                }
            }
            ListNode* second = head;
            while (first->next != nullptr) {
                first = first->next;
                second = second->next;
            }
            // now second ptr is before the to-be-deleted node
            ListNode* nn = second;
            if (n >= 2) {
                nn = nn->next->next;
                delete second->next;
                second->next = nn;

            } else if (n == 1) {
                delete second->next;
                second->next = nullptr;
            } 

            
            return head;




        }
    };