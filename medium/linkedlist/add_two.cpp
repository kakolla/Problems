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
        ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
            ListNode* n = new ListNode();
            ListNode* head = n;
            ListNode* p = nullptr; // previous
    
            int carry = 0;
            int a = 0;
            while (l1 != nullptr && l2 != nullptr) {
                a = (l1->val + l2->val + carry) % 10;
                carry = (l1->val + l2->val + carry) / 10;
                n->val = a;
                ListNode* k = new ListNode();
                n->next = k;
                p = n;
                n = k;
                l1 = l1->next;
                l2 = l2->next;
            }
            n->val += carry; // add carry to last node
            
            if (l1 == nullptr && l2 == nullptr) {
                // delete leading 0
                if (n->val == 0) {
                    p->next = nullptr;
                    delete n;
                }
                return head;
            }
    
    
            // remaining trail
            // pick whichever has left
            ListNode* d = (l1 == nullptr) ? l2 : l1;
    
            while (d != nullptr) {
                a = (d->val + carry) % 10;
                carry = (d->val + carry) / 10;
                n->val = a;
                ListNode* k = new ListNode();
                n->next = k;
                p = n;
                n = k;
                d = d->next;
            }
            n->val += carry; // add carry to last node
            if (n->val == 0) {
                p->next = nullptr;
                delete n;
            }
    
            return head;
        }
    };