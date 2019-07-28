class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        //如果是空的，则一定对称
        if(root == nullptr)
            return true;
        vector<TreeNode*> nodes;
        nodes.push_back(root);
        
        while(nodes.size()>0)
        {
            vector<TreeNode*> nodesNextLayer;
            //将存的左边一半节点与对应位置的右边一半节点比较
            for(int i = 0; i<nodes.size()/2;i++)
            {
                //如果对应位置的节点都不为空，比较值是否相等，并存入左右子节点
                if(nodes[i]!=nullptr&&nodes[nodes.size()-i-1]!=nullptr)
                {
                    if(nodes[i]->val == nodes[nodes.size()-i-1]->val)
                    {
                        nodesNextLayer.push_back(nodes[i]->left);
                        nodesNextLayer.push_back(nodes[i]->right);
                    }
                    else
                        return false;
                }
                //如果对应位置的节点都为空
                else if(nodes[i]==nullptr&&nodes[nodes.size()-i-1]==nullptr)
                    continue;
                else
                    return false;
            }
            //存储右半部分节点
            for(int i = nodes.size()/2; i<nodes.size();i++)
            {
                if(nodes[i]!=nullptr&&nodes[nodes.size()-i-1]!=nullptr)
                {
                    nodesNextLayer.push_back(nodes[i]->left);
                    nodesNextLayer.push_back(nodes[i]->right);
                }
                else
                    continue;
            }
            nodes = nodesNextLayer;
        }
        return true;
    }
};

