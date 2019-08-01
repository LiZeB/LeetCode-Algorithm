#include<map>
class Solution {
public:
    int numTrees(int n) {
        map<pair<int, int>, int> map1;
        return generateTrees(1, n, map1);
    }
    
    int generateTrees(int start, int end, map<pair<int, int>, int> &map1){
        if(start>=end){
            return 1;
        }
        pair<int, int> p0(start, end);
        if(map1.find(p0) != map1.end()){
            // for(auto  iter=map1.begin(); iter != map1.end(); iter ++){
            //     cout<<iter->second <<endl;
            // }
            return map1[p0];
        }
        
        int left, right, nums=0;
        for(int i=start; i<=end; i++){
            left = generateTrees(start, i-1, map1);
            pair<int, int> p1(start, i-1);
            map1[p1] = left;
            right = generateTrees(i+1, end, map1);
            pair<int, int> p2(i+1, end);
            map1[p2] = right;
            nums += left*right;   
        }
        
        return nums;
    }

};
