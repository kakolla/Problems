

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

#include <vector>
using namespace std;

class Solution {
public:
    int maxDepth(TreeNode* root) {
        return maxDepthHeight(root, 0);
    }

    int maxDepthHeight(TreeNode* root, int height)
    {
        if (root == NULL) return 0;

        int lheight = 1 + maxDepthHeight(root->left, height);
        int rheight = 1 + maxDepthHeight(root->right, height);
        if (lheight > rheight) return lheight;
        else return rheight;

    }
};
