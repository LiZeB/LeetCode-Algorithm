#include<iostream>
#include<queue>
#include<vector>
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
// class Solution {
// public:
//     vector<vector<int>> levelOrder(TreeNode* root) {
//         vector<vector<int>> result;
//         queue<TreeNode *> q1;
//         TreeNode *t = root;
        
//         while(t != NULL){
//             cout<<t->val;
//             vector<int> temp;
//             temp.push_back(root->val);
//             result.push_back(temp);
            
//             if(t->left != NULL) {
//                 q1.push(t->left);
//             }
//             if(t->right != NULL) {
//                 q1.push(t->right);   
//             }
//             if(!q1.empty()){
//                 t = q1.front();
//                 q1.pop();
//             }
//             else{
//                 return result;
//             }   
//         }
//     }
// };
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
         vector<vector<int>> res;
        if(!root){
		    return res;
	    }
        queue<TreeNode*> Q;
        TreeNode* p;
        Q.push(root);
        cout<<Q.empty()<<endl;   //很奇怪，这里为什么时0
        while(Q.empty()==0){
            vector<int> a;
            int width=Q.size();
            for(int i=0;i<width;i++){
                p=Q.front();
                a.push_back(p->val);
                Q.pop();
                if(p->left) Q.push(p->left);
                if(p->right) Q.push(p->right);
            }
            res.push_back(a);
        }
    return res;
    }
};
