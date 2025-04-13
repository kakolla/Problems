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
        int height(TreeNode* n, bool& yr) {
            if (n == nullptr) return -1;
            int lheight = 1 + height(n->left, yr);
            int rheight = 1 + height(n->right, yr);

            int height = max(lheight, rheight);
            if (abs(lheight - rheight) > 1) {
                yr = false;
            }
            return height;
        }
        bool isBalanced(TreeNode* root) {
            bool yr = true;
            height(root, yr);
            return yr;
            


        }
    };
    