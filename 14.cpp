#include<iostream>
#include<string>

using namespace std;

//Definition for a binary tree node.
/*struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};*/

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        string s1="", s2="";
        preOrder(p, s1);
        preOrder(q, s2);
        if(s1 == s2){
            return true;
        }
        else{
            return false;
        }
    }
    void preOrder(TreeNode *t, string &s){
        if(t!=NULL){
            s += to_string(t->val);
            preOrder(t->left, s);
            preOrder(t->right, s);
        }
        else{
            s += "null";
        }
    }
};
