class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = len(height) - 1
        start = 0
        end = l
        while start < end:
            temp = (end - start) * min(height[start], height[end])
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
            if temp > max_area:
                max_area = temp
        return max_area

###时间68.56%， 内存0.78%
