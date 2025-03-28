/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
#include <unordered_map>
class Solution {
    public:
        Node* copyRandomList(Node* head) {
            if (head == nullptr) return nullptr;
            Node* n = new Node(head->val);
            n->random = head->random;

            Node* new_head = n;
            Node* prev = n;

            Node* curr = head->next;
            
            unordered_map<Node*, Node*> mp;
            mp[head] = n;


            while (curr) {
                n = new Node(curr->val);
                n->random = curr->random; // for now use the og link
                mp[curr] = n; 

                prev->next = n;
                prev = n;

                curr = curr->next;
                
            }

            // add random pointers
            curr = new_head;
            while (curr) {
                curr->random = mp[curr->random]; // relink it
                curr = curr->next;
                head = head->next;
            }

            


            return new_head;



        }
    };
    