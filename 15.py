class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        print(nums)
        if nums == []:
            return []
        i = 0
        nums.sort()
        list1 = []
        while i < len(nums)-2:
            temp = nums[i]
            j = i+1
            temp1 = nums[j]
            k = len(nums) -1
            temp2 = nums[k]
            print(i, j, k)
            while j < k and j > i:
                sum1 = nums[i] + nums[j] + nums[k]
                #print(temp1)
                if sum1 == 0:
                    list1.append([nums[i], nums[j], nums[k]])
                    if nums[j+1] != temp1 or nums[k-1] != temp2:
                        j += 1
                        k -= 1
                elif sum1 < 0:
                    j += 1
                elif sum1 > 0:
                    k -= 1
            while i< len(nums)-2 and nums[i] == temp:
                i +=1
                
        return list1
