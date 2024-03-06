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
        dic1 = {}
        dic2 = {}

        for c in s:
            dic1[c] = dic1.get(c, 0) + 1
        for c in t:
            dic2[c] = dic2.get(c, 0) + 1
        
        return dic1 == dic2
    
# 1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = {}

        for i,n in enumerate(nums):
            diff = target - n
            if n in count.keys():
                return [count[n], i]
            else:
                count[diff] = i

# 49. Group Anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}

        for str in strs:
            sorted_string = "".join(sorted(str))
            if sorted_string not in res:
                res[sorted_string] = []
            
            res[sorted_string].append(str)
        
        return list(res.values())

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
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)
        
        arr = []

        for x in range(len(nums), 0, -1):
            if x in frq:
                for i in frq[x]:
                    arr.append(i)

        return [arr[x] for x in range(0, k)]

# 1929. Concatenation of Array
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums

# 1299. Replace Elements with Greatest Element on Right Side
    # Timed out on a very large test case 
class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if len(arr) == 1:
            return [-1]
        
        res = []

        for i in range(len(arr)):
            if i < len(arr) - 2:
                m = max(arr[i+1:])
                res.append(m)
            elif i == len(arr) - 2:
                res.append(arr[i + 1])
        
        res.append(-1)
        return res

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

# 238. Product of Array Except Self
    class Solution(object):
        def productExceptSelf(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """

            res = []

            tmp = 1

            for n in nums:
                res.append(tmp)
                tmp *= n

            tmp = 1
            for i in reversed(range(len(nums))):
                res[i] *= tmp
                tmp *= nums[i]

            return res

# 36. Valid Sudoku

class Solution(object):
    def isValidSudoku(self, board):
        return (self.is_row_valid(board) and
            self.is_col_valid(board) and
            self.is_square_valid(board))

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True

    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True

    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)

# 128. Longest Consecutive Sequence
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        max_con = 0

        while nums:
            first = last = nums.pop()
            while first - 1 in nums:
                first -= 1
                nums.remove(first)
            while last + 1 in nums:
                last += 1
                nums.remove(last)
            max_con = max(max_con, last - first + 1)
        
        return max_con

# 58. Length of Last Word
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        words = s.split()
        return len(words[-1])

# 392. Is Subsequence
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
                prefix = prefix[:-1]
        
        return prefix

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

# 12345 