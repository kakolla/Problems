













#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int val;
    int key;
    Node* next;
    Node* prev;
};

class LRUCache {
public:
    int capacity;
    unordered_map<int, Node*> m;
    Node* hd;
    Node* tl;
    int sz;

    LRUCache(int capacity) {
        this->capacity = capacity;
        this->hd = nullptr;
        this->tl = nullptr;
        this->sz = 0;
    }
    
    void remove_node(int key) {
        Node* n = this->m[key];

        // if head
        // cout << n << endl;
        Node* prev = n->prev;
        Node* next = n->next;
        if (this->hd == n) {
            this->hd = n->next;
        }
        if (this->tl == n) {
            this->tl = n->prev;
        }
        
        if (prev)  {
            prev->next = n->next;
        }
        if (next) {
            next->prev = n->prev;
        }
        this->m.erase(key);
        delete n;
    }

    void place_node(int key, int val) {
        // place at front
        Node* n = new Node();
        n->val = val;
        n->key = key;
        this->m[key] = n;

        if (hd) {
            hd->prev = n;
            n->next = hd;
        }
        else {
            this->tl = n;
        }
        this->hd = n;

    }

    int get(int key) {
        // not found
        if (this->m.find(key) == this->m.end()) return -1;

        // update to list
        int val = m[key]->val;
        this->remove_node(key);
        this->place_node(key,val );

        // get val
        return val;
        
    }
    
    void put(int key, int value) {
        // if there, update
        if (m.find(key) != m.end()) {
            this->remove_node(key);
            this->sz--;
        } else {
            if (this->sz == this->capacity) {
                // remove lru
                this->remove_node(this->tl->key);
                this->sz--;
            }

        }

        this->place_node( key,  value); // at front
        this->sz++;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
