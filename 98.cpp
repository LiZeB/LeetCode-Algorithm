#include<vector>
#include<algorithm>

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
    bool isValidBST(TreeNode* root) {
//此题看似简单，实际很难。要特别注意隔了好几层的节点也有一定的大小关系,如果不知道这个，就可能写成我下面这种简单的递归
//         if(root == NULL) {
//             return true;
//         }
//         if((root->right == NULL) && (root->left == NULL)){
//             return true;
//         }
//         bool left_flag, right_flag;
//         if(root->left != NULL){
//             if(root->val < root->left->val)
//                 return false;
//             else
//                 left_flag = isValidBST(root->left);
//         }
        
      
//         if(root->right != NULL) {
//             if(root->val > root->right->val)
//                 return false;
//             else
//                 right_flag =  isValidBST(root->right);
//         }
//         if(left_flag  && right_flag)
//             return true;
//         else{
//             return false;
//         }
        if(root == NULL) return true;
        
        vector<int> v1;
        inOrder(root, v1);
        vector<int> v2(v1);
        
        sort(v1.begin(), v1.end());
        if(v1 == v2){
            for(auto iter = v1.begin(); iter != (v1.end()-1); iter ++){
                if((*iter) == (*(iter+1))){
                    return false;
                }
            }
            return true;
        }
        else{
            return false;
        }
    }
    void inOrder(TreeNode * root, vector<int> &v1){
        if(root != NULL){
            inOrder(root->left, v1);
            v1.push_back(root->val);
            inOrder(root->right, v1);
        }
    }
     
};
