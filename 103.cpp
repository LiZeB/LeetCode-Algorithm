#include<queue>
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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        queue<TreeNode*> q1;
        vector<vector<int>> result;
        if(root == NULL){
            return vector<vector<int>>();
        }
        q1.push(root);
        int i = 0;
        while(!q1.empty()){
            vector<int> temp;
            TreeNode *t;
            int N = q1.size();
            for(int j=0; j<N; j++){
                t = q1.front();
                temp.push_back(t->val);
                q1.pop();
                if(t->left != NULL) q1.push(t->left);
                if(t->right != NULL) q1.push(t->right);     
            }
            if(i%2!=0){
                temp = vector(temp.rbegin(), temp.rend());
            }
            result.push_back(temp);
            i++;
        }
        return result;
    }
};
