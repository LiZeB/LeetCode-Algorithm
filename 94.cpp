#include<iostream>
using namespace std;
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result, temp1, temp2;
        if(root!=NULL){
            temp1 = inorderTraversal(root->left);
            for(auto iterator = temp1.begin(); iterator != temp1.end(); iterator++){
                result.push_back(*iterator);
            }
            result.push_back(root->val);
            temp2 = inorderTraversal(root->right);
             for(auto iterator = temp2.begin(); iterator != temp2.end(); iterator++){
                result.push_back(*iterator);
            }
        }
        return result;
    }
};
