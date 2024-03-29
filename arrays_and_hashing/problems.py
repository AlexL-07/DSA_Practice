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
    def canPlaceFlowers(self, flowerbed):
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


# 705. Design HashSet

class MyHashSet(object):

    def __init__(self):
        self.d = {}
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.d[key] = 1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.d[key] = 0
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return self.d.get(key, 0) != 0
        


    # Your MyHashSet object will be instantiated and called as such:
    # obj = MyHashSet()
    # obj.add(key)
    # obj.remove(key)
    # param_3 = obj.contains(key)


# 706. Design HashMap

class MyHashMap(object):

    def __init__(self):
        self.data = [None] * 1000001
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.data[key] = value
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = self.data[key]
        if val != None:
            return val
        else:
            return -1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.data[key] = None
        


        # Your MyHashMap object will be instantiated and called as such:
        # obj = MyHashMap()
        # obj.put(key,value)
        # param_2 = obj.get(key)
        # obj.remove(key)


# 919. Sort an Array


class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def quickSort(nums):
            if len(nums) <= 1:
                return nums
            
            piv = random.choice(nums)
            lt, eq, gt = [], [], []

            for n in nums:
                if n < piv:
                    lt.append(n)
                elif n > piv:
                    gt.append(n)
                else:
                    eq.append(n)
            
            return quickSort(lt) + eq + quickSort(gt)
        return quickSort(nums)


# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums):
        res = []
        
        acc = 1
        for n in nums:
            res.append(acc)
            acc *= n

        acc = 1
        for i in reversed(range(len(nums))):
            res[i] *= acc
            acc *= nums[i]
            
        return res


    # The product of elements except the ith one is equal to a product of elements on the left side and on the right side of that element. 
    # So the idea is to do two passes over the input nums and use an auxiliary list res to store intermediate results. 
    # First pass we do from the start to the end and on each iteration we store the accumulated product in the res at the according index such that the value of the res at the ith index equal to product of all elements in nums starting from 0 to i-1, i.e: res[i] = product(nums[0:i-1]). 
    # The second pass we do from the end to the start of the nums. We again accumulate a product of met elements and modify the res such that the value at the index i is equal to the product of the value at this index and accumulated value from the pass. In the end, the res is the required answer.

    # Time: O(n) for two passes over nums
    # Space: O(1) since the result doesn't count against the space complexity


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
        maxLen = 0

        while nums:
            first = last = nums.pop()
            while first - 1 in nums:
                first -= 1
                nums.remove(first)
            while last + 1 in nums: 
                last += 1
                nums.remove(last)
            maxLen = max(maxLen, last - first + 1)
        
        return maxLen 


# 75. Sort Colors

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0 
        blue = len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
            
        return nums

    # This is a dutch partitioning problem. We are classifying the array into four groups: red, white, unclassified, and blue. 
    # Initially we group all elements into unclassified. 
    # We iterate from the beginning as long as the white pointer is less than the blue pointer.

    # If the white pointer is red (nums[white] == 0), we swap with the red pointer and move both white and red pointer forward. 
    # If the pointer is white (nums[white] == 1), the element is already in correct place, so we don't have to swap, just move the white pointer forward. 
    # If the white pointer is blue, we swap with the latest unclassified element.


# 535. Encode and Decode TinyURL

class Codec:
    codeDB = defaultdict()
    urlDB = defaultdict()
    chars = string.ascii_letters + string.digits

    def getCode(self):
        code = ''.join(random.choice(self.chars) for i in range(6))
        return "http://tinyurl.com/" + code

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """

        if longUrl in self.urlDB:
            return self.urlDB[longUrl]
        
        code = self.getCode()
        while code in self.codeDB:
            code = getCode()
        
        self.codeDB[code] = longUrl
        self.urlDB[longUrl] = code
        return code
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.codeDB[shortUrl]


# 554. Brick Wall

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        sumMap, maxSum = {}, 0

        for i in range(len(wall)):
            currSum = 0
            for j in range(len(wall[i])-1):
                currSum += wall[i][j]
                if currSum not in sumMap:
                    sumMap[currSum] = 0
                sumMap[currSum] += 1
                maxSum = max(maxSum, sumMap[currSum])
        
        return len(wall) - maxSum
    


# 122. Best Time to Buy and Sell Stock II
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits = []

        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profits.append(prices[i + 1] - prices[i])
        
        return sum(profits)
    

# 560. Subarray Sum Equals K

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        res = 0 
        pref_sum = 0
        d = {0:1}

        for n in nums:
            pref_sum = pref_sum + n

            if pref_sum - k in d:
                res = res + d[pref_sum - k]
            
            if pref_sum not in d:
                d[pref_sum] = 1
            else:
                d[pref_sum] = d[pref_sum] + 1
        
        return res


# 1930. Unique Length-3 Palindromic Subsequences
class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = {}

        for i, c in enumerate(s):
            if c not in d:
                d[c] = [i, i]
            else:
                d[c][1] = i
        

        res = 0

        for c, (start_idx, end_idx) in d.items():
            res += len(set(s[start_idx + 1:end_idx]))

        return res


# 1963. Minimum Number of Swaps to Make the String Balanced
class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        for i in s:
            if i == "[":
                count += 1  # increment only if we encounter an open bracket. 
            else:
                if count > 0:  #decrement only if count is positive. Else do nothing and move on. This is because for the case " ] [ [ ] " we do not need to in
                    count -= 1
        return (count + 1) // 2
       

# 2001. Number of Pairs of Interchangeable Rectangles
class Solution(object):
    def interchangeableRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """

        # map to track ratio counts
        ratio_map = {}
        total = 0
        for rect in rectangles:
            ratio = float(rect[0]) / float(rect[1])
            ratio_map[ratio] = ratio_map.get(ratio, 0) + 1
        
        # we are looking at PAIRs not PERMUTATIONs so we don't use factorial
        for k, v in ratio_map.items():
            total += (v * (v - 1)) // 2
        
        return total


# 2002. Maximum Product of the Length of Two Palindromic Subsequences 
class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        arr = []

        for mask in range(1, 1<<n):
            subseq = ''
            for i in range(n):
                if mask & (1 << i) > 0:
                    subseq += s[i]
            if subseq == subseq[::-1]:
                arr.append((mask, len(subseq)))
        
        result = 1

        for (mask1, len1), (mask2, len2) in product(arr, arr):
            if mask1 & mask2 == 0:
                result = max(result, len1 * len2)
        
        return result

# 28. Find the Index of the First Occurence in a String

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        
        return -1

# using built in python method (slightly slower)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
    
# 1822. Sign of the Product of an Array
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prod = 1

        for n in nums:
            prod *= n

        if prod > 0:
            return 1
        elif prod < 0:
            return -1
        else:
            return 0

# 2215. Find the Difference of Two Arrays
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        res = []
        res1 = set()
        res2 = set()

        for n in nums1:
            if n not in nums2:
                res1.add(n)
        
        for n in nums2:
            if n not in nums1:
                res2.add(n)

        res.append(list(res1))
        res.append(list(res2))
        
        return res

    # one liner
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        return [set(nums1) - set(nums2), set(nums2) - set(nums1)]

# 1603. Design Parking System
class ParkingSystem(object):

    __slot__ = ['_parking']

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self._parking = {
            1: big,
            2: medium,
            3: small
        }
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        available_spots = self._parking[carType]
        if available_spots:
            self._parking[carType] = available_spots - 1
            return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

# 438. Find All Anagrams in a String
class Solution(object):
    def findAnagrams(self, s, p):

        n = len(s)
        m = len(p)
        
        p = Counter(p)                    # Convert list of anagram letters to a Counter (hashtable)
        ans = []
           
        window = None
        for i in range(0,n-m+1):
            if i == 0: 
                window = Counter(s[:m])   # Initialize window with beginning of s => length = length of anagram letters
            else:    
                window[s[i-1]] -= 1       # Move window to right: 1. remove character on the left
                window[s[i+m-1]] += 1     #                       2. add character on the right
            if len(window - p) == 0:      # Check if window is anagram (direct comparison of counters does not work with 0 entries)
                ans.append(i)
                
        return ans

# 179. Largest Number
    # build-in function
    def largestNumber1(self, nums):
        if not any(nums):
            return "0"
        return "".join(sorted(map(str, nums), cmp=lambda n1, n2: -1 if n1+n2>n2+n1 else (1 if n1+n2<n2+n1 else 0)))

    # bubble sort
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in range(len(nums), 0, -1):
            for j in range(i - 1):
                if not self.compare(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return str(int("".join(map(str, nums))))
    
    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)

    # selection sort
    def largestNumber3(self, nums):
        for i in range(len(nums), 0, -1):
            tmp = 0
            for j in range(i):
                if not self.compare(nums[j], nums[tmp]):
                    tmp = j
            nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
        return str(int("".join(map(str, nums))))

    # insertion sort
    def largestNumber4(self, nums):
        for i in range(len(nums)):
            pos, cur = i, nums[i]
            while pos > 0 and not self.compare(nums[pos-1], cur):
                nums[pos] = nums[pos-1]  # move one-step forward
                pos -= 1
            nums[pos] = cur
        return str(int("".join(map(str, nums))))

    # merge sort        
    def largestNumber5(self, nums):
        nums = self.mergeSort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums))))

    def mergeSort(self, nums, l, r):
        if l > r:
            return 
        if l == r:
            return [nums[l]]
        mid = l + (r-l)//2
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid+1, r)
        return self.merge(left, right)

    def merge(self, l1, l2):
        res, i, j = [], 0, 0
        while i < len(l1) and j < len(l2):
            if not self.compare(l1[i], l2[j]):
                res.append(l2[j])
                j += 1
            else:
                res.append(l1[i])
                i += 1
        res.extend(l1[i:] or l2[j:])
        return res

    # quick sort, in-place
    def largestNumber(self, nums):
        self.quickSort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums)))) 

    def quickSort(self, nums, l, r):
        if l >= r:
            return 
        pos = self.partition(nums, l, r)
        self.quickSort(nums, l, pos-1)
        self.quickSort(nums, pos+1, r)

    def partition(self, nums, l, r):
        low = l
        while l < r:
            if self.compare(nums[l], nums[r]):
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low

# 523. Continuous Subarray Sum
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        dic = {0: -1}
        s = 0

        for i, n in enumerate(nums):
            s = (s + n) % k

            if s not in dic:
                dic[s] = i
            else:
                if i - dic[s] >= 2:
                    return True
        
        return False
    # https://leetcode.com/problems/continuous-subarray-sum/solutions/1929464/greatly-explained-hashmap-prefixsum-in-python-time-o-n-space-o-min-n-k-easy-to-understand/