# 217. Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = set()
        for n in nums:
            if n in count:
                return True
            else:
                count.add(n)


# 242. Valid Anagram
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1, dic2 = {}, {}
        for x in s: 
            dic1[x] = dic1.get(x, 0) + 1
        for x in t:
            dic2[x] = dic2.get(x, 0) + 1
        return dic1 == dic2 


# 1. Two Sum 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = {}
        for i in range(len(nums)):
            if target - nums[i] in index:
                return [index[target - nums[i]], i]
            index[nums[i]] = i
        return []


# 49. Group Anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}

        for str in strs:
            sorted_string = ''.join(sorted(str))
                # seperator.join() joins characters or strings together, based off of the seperator
                # sorted() returns a sorted list of the specified iterable object, in this case the characters  
            if sorted_string not in res:
                res[sorted_string] = []
            
            res[sorted_string].append(str)
        
        
        return list(res.values())
            # the list() constructor returns a list (array pretty much) in python


# 1929. Concatenation of Array

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)

        for i in range(0, length):
            nums.append(nums[i])
        

        return nums


# 347. Top K Frequent Elements

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hs = {}
        frq = {}

        for i in range(0, len(nums)):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else: 
                hs[nums[i]] += 1
        

        for z, v in hs.items():
            # dictionary.items() returns a view object that contains the key-value pairs of the dictionary, as tuples in a list 
            # z here is the value
            # v here is the key
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)
        

        arr = []

        for x in range(len(nums), 0, -1):
            # range(start, stop, step), with -1 we are going to be subtracting 1 from len(nums) until we reach 0
            # default step is +1 if we do not include a step 
            if x in frq:
                for i in frq[x]:
                    arr.append(i)


        return [arr[x] for x in range(0, k)]


# 1299. Replace Elements with Greatest Element on Right Side 
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        m = -1
        i = len(arr) - 1
        while i >= 0:
            temp = arr[i]
            arr[i] = m
            if temp > m:
                m = temp
            i -= 1
        return arr

# 393. Is Subsequence
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)

# 58. Length of Last Word
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        words = s.split(" ")
        
        i = len(words) - 1
        
        while len(words[i]) == 0:
            del words[i]
            i -= 1

        return len(words[-1])

    # better solution 
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        words = s.split()
        # string.split() with no parameters gets rid of all empty spaces but does not split the words up into characters
        # to split words up into characters use list(string)
        return len(words[-1])
    

# 14. Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = strs[0]

        for s in strs:
            while not s.startswith(prefix):
                # string.startswith(str) returns a boolean if the string starts with the same characters as the input string
                prefix = prefix[:-1]
                    # if string.startswith(str) returns false, we will keep removing the last character until it returns true to exit the while loop 
        
        return prefix
