# 125. Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return True
        
        alphabet = set('abcdefghijklmnopqrstuvwxyz1234567890')
        newStr = ""

        for c in s:
            if c.lower() in alphabet:
                newStr += c.lower()

        return newStr == newStr[::-1]

# 680. Valid Palindrome II
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h = 0
        t = len(s) - 1

        while h < t:
            if s[h] != s[t]:
                return s[h:t] == s[h:t][::-1] or s[h + 1:t + 1] == s[h + 1:t + 1][::-1]
            h = h + 1
            t = t - 1
        
        return True

# 1984. Minimum Difference Between Highest and Lowest of K Scores
class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        
        nums.sort()
        res = nums[k - 1] - nums[0]

        for i in range(k, len(nums)):
            res = min(res, nums[i] - nums[i - k + 1])
        
        return res