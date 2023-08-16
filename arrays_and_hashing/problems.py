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


# 169. Majority Element

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        majority = len(nums)/2
        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
                if count[n] > majority:
                    return n
            else:
                count[n] = 1


# 496. Next Greater Element 1


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        res = []

        for i, n in list(enumerate(nums1)):
            ind = nums2.index(n)
            flag = False
            for i in range(ind, len(nums2)):
                if n < nums2[i]:
                    res.append(nums2[i])
                    flag = True
                    break
            if not flag:
                res.append(-1)

                        
        
        return res

    # O(n) Solution

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        map = {} # map for next greater element
        stack = []
        for num in nums2:
            while stack and stack[-1] < num: # Pop elements from stack and update map with next greater element
                map[stack.pop()] = num
            stack.append(num) # Push current element onto stack
        for i in range(len(nums1)): # Check if each element in nums1 has a next greater element in map
            nums1[i] = map.get(nums1[i], -1) # Update element in nums1 with next greater element or -1
        return nums1


# 724. Find Pivot Index

# Time Complexity : O(n)
# Space Complexity : O(1)
class Solution(object):
    def pivotIndex(self, nums):
        # Initialize leftSum & rightSum to store the sum of all the numbers strictly to the index's left & right respectively...
        leftSum, rightSum = 0, sum(nums)
        # Traverse elements through the loop...
        for idx, ele in enumerate(nums):
            # enumerate(iterable, Start(not necessary)) returns a list of tuples that contains the index and element at that index (ex. [(idx, ele), (idx1, ele1)])
                # Iterable: any object that supports iteration
                # Start: the index value from which the counter is to be started, by default it is 0
            rightSum -= ele
            # If the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right...
            if leftSum == rightSum:
                return idx      # Return the pivot index...
            leftSum += ele
        return -1       # If there is no index that satisfies the conditions in the problem statement...


# 303. Range Sum Query - Immutable


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """

        return sum(self.nums[left:right+1])
    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # param_1 = obj.sumRange(left,right)


# 448. Find All Numbers Disappeared in an Array


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        range_set = set(range(1, len(nums) + 1))
        num_set = set(nums)

        return list(range_set - num_set)
            # you can subtract between sets to remove duplicates
            # this gives us a new set which we can make into a list with list()


# 1189. Maximum Number of Balloons

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        b_count = {"b":0, "a":0, "l":0, "o":0, "n":0}

        for char in text:
            if char.lower() in b_count:
                b_count[char.lower()] += 1
        

        counter = 0
        while b_count["b"] > 0 and b_count["a"] > 0 and b_count["l"] > 0 and b_count["o"] > 0 and b_count["n"] > 0:
            if (b_count["b"] - 1) >= 0 and (b_count["a"] - 1) >= 0 and (b_count["l"] - 2) >= 0 and (b_count["o"] - 2) >= 0 and (b_count["n"] - 1) >= 0:
                counter += 1
            b_count["b"] -= 1
            b_count["a"] -= 1
            b_count["l"] -= 2
            b_count["o"] -= 2
            b_count["n"] -= 1
                
        
        return counter


    # Much better solution 

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        strs = ['b', 'a', 'l', 'o', 'n']
        counts = [0] * 5

        for i in range(5):
            counts[i] = text.count(strs[i])
        
        counts[2] = counts[2] // 2
        counts[3] = counts[3] // 2

        return min(counts)
    

# 290. Word Pattern

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        new_str = []
        words = s.split()
        dic = {}

        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)): 
            return False
        
        for idx, c in enumerate(pattern):
            if c in dic:  
                if dic[c] != words[idx]: 
                    return False  
            else:
                dic[c] = words[idx]

            if c in dic:
                new_str.append(dic[c])
        

        new_s = " ".join(new_str) 
        return new_s == s 
            