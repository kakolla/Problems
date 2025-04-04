/*
Diameter is the largest path we've seen (like taking a bin tree and pulling it stretched)
Diameter of a node i is left_height + r_height
keep track of the largest we've seen so far up the recursion, that's it
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

 class Solution {
    public:
        std::pair<int, int> recurse(TreeNode* node) {
            if (node == nullptr) {
                return pair<int, int>(-1, 0);
            }

            pair<int, int> t = recurse(node->left);
            int l_height = 1 + t.first;
            pair<int, int> t2 = recurse(node->right);
            int r_height = 1 + t2.first;
            
            // max diameter we've seen
            int max_d = max(t.second, t2.second);
            max_d = max(max_d, l_height + r_height);
            return std::pair<int, int>(
                max(l_height, r_height),
                max_d
            );
                       
        }
        int diameterOfBinaryTree(TreeNode* root) {
            return recurse(root).second;
            
        }
    };
    