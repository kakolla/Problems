/*
Two pointers approach
Use a slow pointer
And a fast pointer (moves ahead by two)
If the fast pointer catches up (==) the slow pointer, that means
there is a cycle
*/

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
        bool hasCycle(ListNode* head) {
            ListNode* p1 = head;
            ListNode* p2 = head;
    
            while (head != nullptr) {
                if (p2->next == nullptr) return false;
                p2 = p2->next->next; // fast pointer
                if (p2 == nullptr) return false;
                p1 = p1->next; // slow pointer
                if (p1 == p2) {
                    return true;
                }
    
            }
            return false;
            
        }
    };
    