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

# 219. Contains Duplicate II
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
    
# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        s = 0 
        res = 0

        for i in range(0, k - 1):
            s += arr[i]
        
        for i in range(k - 1, len(arr)):
            s += arr[i]
            if s / k >= threshold:
                res += 1
            s -= arr[i - k + 1]
        
        return res

# 3. Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0
        
        lengths = [1] # this is the minimum length possible for this problem, it's ok to initiate the res array with this 
        sub = ""

        i = 0

        while i < len(s):
            if s[i] not in sub:
                sub += s[i]
                lengths.append(len(sub))
                i += 1
            else:
                i = i - len(sub) + 1
                sub = ""
        
        return max(lengths)

    # Better solution using a dictionary to store seen and its index
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0 
        seen = {}
        output = 0

        for right, curr in enumerate(s):
            if curr in seen:
                left = max(left, seen[curr] + 1)
            output = max(output, right - left + 1)
            seen[curr] = right
        
        return output
        