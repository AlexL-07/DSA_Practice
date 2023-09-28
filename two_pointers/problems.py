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

# 1768. Merge String Alternatively
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        newStr = ""

        leng = len(word1)
        leng2 = len(word2)
        longest = word1
        # x = 0

        if len(word2) > len(word1):
            leng = len(word2)
            leng2 = len(word1)
            longest = word2
        
        for i in range(leng2):
            newStr += word1[i]
            newStr += word2[i]
            # x = i
        
        newStr += longest[i+1:]
            # I guess the variable i saves itself as max number of the passed in range even outside the loop 
        
        return newStr

    # Better solution
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        newStr = ""

        for i in range(min(len(word1), len(word2))):
            newStr += word1[i] + word2[i]
        
        return newStr + word1[i+1:] + word2[i+1:]


# 344. Reverse String
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]

            i += 1
            j -= 1

# 88. Merge Sorted Array
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # should merge nums2 into nums1 
        a = m - 1
        b = n - 1
        ind = m + n - 1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[ind] = nums1[a]
                a -= 1
            else:
                nums1[ind] = nums2[b]
                b -= 1
            ind -= 1

# 283. Move Zeroes
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        orig = len(nums)
        i = 0

        while i < orig:
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                orig -= 1
            else:
                i += 1


# 26. Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums))
        return len(nums)

    # using two pointers, much slower
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0
        second = 1

        while second in range(len(nums)):
            if nums[first] == nums[second]:
                second += 1
            else:
                nums[first + 1] = nums[second]
                second += 1
                first += 1
        
        return first + 1