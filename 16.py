#inclde <iostream>

using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int sum1, temp_sum, previous_delta = -1, delta, flag = 1;
        
        for(int i=0; i<nums.size(); i++){
            for(int j=i+1; j<nums.size(); j++){
                if(i>=j) continue;
                sum1 = nums[i] +nums[j];
                for(int k=j+1; k<nums.size(); k++){
                    if(i>=k) continue;
                    if(j>=k) continue;
                    temp_sum = sum1 + nums[k];
                    if(previous_delta == -1)  previous_delta = abs(target - temp_sum);
                    delta = abs(target - temp_sum);
                    if(delta <= previous_delta) {
                        previous_delta = delta;
                        flag = ((temp_sum-target)>=0)? 1:-1;
                    }
                }
            }
        }
        return (flag* previous_delta + target);
    }
};
