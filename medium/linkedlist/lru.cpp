#include <unordered_map>
#include <iostream>
using namespace std;
class LRUCache {

    struct Node {
        Node* next;
        Node* prev;
        int val;
        int key;
        Node(int key, int val) {
            this->val = val;
            this->prev = nullptr;
            this->next = nullptr;
            this->key = key;
        }

    };


    public:
        int capacity;
        int size;
        Node* head; // least recently used
        Node* tail; // most recently used
        unordered_map<int, Node*> mp;

        LRUCache(int capacity) {   
            this->size = 0;
            this->capacity = capacity;
            head = nullptr;
            tail = head;
        }

        void bringToFront(Node* cur, int key) {
            if (tail == cur) return; // already at front
            Node* prev = cur->prev;
            Node* next = cur->next;
            // case: prev exists
            if (prev) prev->next = next;
            else head = next;

            // case: next exists
            if (next) next->prev = prev;

            // update head
            if (head) head->prev = nullptr;

            tail->next = cur;
            cur->prev = tail;
            cur->next = nullptr;
            tail = cur;
        }
        
        int get(int key) {
            if (mp.find(key) == mp.end()) {
                cout << "get(" << key << ") is nullptr" << endl;
                return -1;
            } else {
                // bring to front; Most recently used
                Node* cur = mp[key];
                bringToFront(cur, key);
                return cur->val;
                
            }
            
        }
        
        void put(int key, int value) {
            if (size == 0) {
                Node* cur = new Node(key, value);
                mp[key] = cur;
                size++;
                head = cur;
                tail = cur;

            } 
            else if (size < capacity) {
                if (mp.find(key) == mp.end()) {
                    Node* cur = new Node(key, value);
                    mp[key] = cur;
                    size++;
                    // add to end of LL
                    tail->next = cur;
                    cur->prev = tail;
                    tail = cur;
                } else if (mp.find(key) != mp.end()) {
                    // if key exists
                    Node* cur = mp[key];
                    cur->val = value;
                    // bring to front; Most recently used
                    bringToFront(cur, key);
                    return;
                    
                }
            } else if (size == capacity) {
                if (head == tail) {
                    // if capacity is 1, delete entries
                    mp.erase(head->key);
                    delete head;

                    // create entry
                    head = new Node(key, value);
                    mp[key] = head;
                    tail = head;
                    return;
                }
                // logic to replace Least recently used
                
                // first check if key exists
                if (mp.find(key) != mp.end()) {
                    // if key exists
                    Node* cur = mp[key];
                    cur->val = value;
                    // bring to front; Most recently used
                    bringToFront(cur, key);
                    return;
                    
                }


                cout << "MAX capacity" << endl;
                // remove head (LRU) & update map
                Node* temp = head;
                head = head->next;
                if (head) head->prev = nullptr;
                mp.erase(temp->key); // IMPORTANT
                delete temp;
                size--;
                
                // push new Node to end (MRU)
                Node* cur = new Node(key, value);
                mp[key] = cur;
                tail->next = cur;
                cur->prev = tail;
                tail = cur;
                size++;

            }

        }
    };
    