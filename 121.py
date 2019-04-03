class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Bad Case1
        if prices == []:
            return 0
        #Bad Case2
        if len(prices) == 1:
            return 0
        max_sum = prices[1] - prices[0]
        l = len(prices)
        min_value = prices[0]
        for i in range(1, l):
            min_value = min(min_value, prices[i])
            max_sum = max(max_sum, prices[i]-min_value)

        return max_sum
        
