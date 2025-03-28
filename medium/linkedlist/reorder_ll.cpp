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




 class Solution
 {
 public:
     void reorderList(ListNode *head)
     {
         if (head->next == nullptr) return; // size 1
 
         
         // get size
         ListNode* curr = head;
         int s = 0;
         while (curr != nullptr)
         {
             s++;
             curr = curr->next;
 
         }
         // get 2nd half off ll
         ListNode* curr2 = head;
         for (int i = 0; i < s/2; ++i) {
             curr2 = curr2->next;
         }
 
         // reverse 2nd half 
         ListNode* prev = curr2;
         curr2 = curr2->next;
         prev->next = nullptr;
         
         while (curr2 != nullptr) {
             ListNode* next = curr2->next;
             curr2->next = prev;
             prev = curr2;
             curr2 = next;
             
         }
         curr2 = prev;
 
         // stitch back head & curr2
         ListNode* first = head;
         ListNode* second = curr2;
 
         while (second) {
             
             ListNode* tmp1 = first->next;
             ListNode* tmp2 = second->next;
             if (tmp1 == nullptr || tmp2 == nullptr) break;
 
             first->next = second;
             second->next = tmp1;
 
             first = tmp1;
             second = tmp2;
         }
 
         
     }
 };