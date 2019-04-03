class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, element1 in enumerate(nums):
            for j, element2 in enumerate(nums[i+1:], i+1):
                if element2 + element1 == target:
                        return [i, j]
