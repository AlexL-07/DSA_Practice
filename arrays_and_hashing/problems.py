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


# 118. Pascal's Triangle
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        
        triangle = [[1], [1, 1]]
        
        if numRows == 2:
            return triangle

        i = 1
        while i < numRows - 1:
            row = []
            j = 0
            x = 1
            while x < len(triangle[i]):
                sum = triangle[i][j] + triangle[i][x]
                row.append(sum)
                j += 1
                x += 1
            
            row.insert(0, 1)
            row.append(1)
            triangle.append(row)
            i += 1
        
        return triangle
    

# 27. Remove Element
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        count = 0
        for n in nums: 
            if n != val:
                nums[count] = n
                count += 1

        return count


# 929. Unique Email Address
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()

        for email in emails:
            words = email.split("@")
            name = words[0]
            domain = words[1]
            for char in name:
                if char == ".":
                    name = "".join(words[0].split("."))
            ind = name.find("+")
            if ind != -1:
                name = name[0:ind]
            new_email = name + "@" + domain
            unique.add(new_email)
        
        return len(unique)


    # cleaner way to do this
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()

        for email in emails:
            local, domain = email.split("@")
            tmp = ""
            for c in local:
                if c == ".": 
                    continue
                elif c == "+": 
                    break
                else: 
                    tmp += c
            unique.add(tmp + "@" + domain)
        
        return len(unique)
    

# 205. Isomorphic Strings

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        trans = {}
        new_str = ""

        for i in range(0, len(s)):
            trans[s[i]] = t[i]
        
        values = trans.values()

        if len(values) != len(set(values)):
            return False
            # this condition checks if there are duplicate values, because sets don't allow for duplicates the length would be different
        
        for i in range(0, len(s)):
            new_str += trans[s[i]]

        return new_str == t

    # solution without dictionary 
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True
        return False
    
    # Efficient solution 
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        zipped_set = set(zip(s, t))
            # zip function would pair the first item of first iterator to the first item of second iterator and make tuples out of these pairs.
            # set() would remove duplicate items from the zipped tuple.
        return len(zipped_set) == len(set(s)) == len(set(t))


# 605. Can Place Flowers
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return n <= 1
            else:
                return 0 == n
    
        count = 0 
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 1
            elif i == 0 and flowerbed[i + 1] != 1:
                count += 1
                i += 1
            elif i == len(flowerbed) - 1 and flowerbed[i - 1] != 1:
                count += 1
                i += 1
            elif flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                count += 1
                i += 1
            i += 1
        
        return count >= n


    # cleaner solution 
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] ==0 and flowerbed[i-1] !=1 and flowerbed[i+1] !=1:
                n -= 1
                # instead of keeping a count you can just decrease n until it is 0 or less than 0
                flowerbed[i] =1
                
        return n <= 0
            