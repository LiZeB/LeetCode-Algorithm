class Solution:
    def maxSubArray(self, nums: List[int]) -> int:     
        sum1 = 0
        max_sum = -2**31
        for temp in nums:
            if sum1 > 0:
                sum1 += temp
            else:
                sum1 = temp
            max_sum = max(sum1, max_sum)
            
        return max_sum
