# 121. Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        left = 0 
        right = 1
        max_profit = 0

        while right < len(prices):
            curr = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(curr, max_profit)
            else:
                left = right
            right += 1
        
        return max_profit 

# Contains Duplicate II
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        dic = {}

        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        
        return False