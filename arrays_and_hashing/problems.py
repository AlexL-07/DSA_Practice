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
            if x in frq:
                for i in frq[x]:
                    arr.append(i)


        return [arr[x] for x in range(0, k)]
