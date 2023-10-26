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
        nums[:] = sorted(set(nums))     # nums[:] = replaces element in place
        return len(nums)                # nums =  doesn't replace elements in the original list.

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

# 80. Remove Duplicates from Sorted Array II
class Solution(object):
    def removeDuplicates(self, nums):
        # Initialize an integer k that updates the kth index of the array...
        # only when the current element does not match either of the two previous indexes. ...
        k = 0
        # Traverse all elements through loop...
        for i in nums:
            # If the index does not match elements, count that element and update it...
            if k < 2 or i != nums[k - 2]:
                nums[k] = i
                k += 1
        return k       # Return k after placing the final result in the first k slots of nums...

# 167. Two Sum II - Input Array Is Sorted
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        diffs = {}

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in diffs:
                return [diffs[diff], i + 1]
            else: 
                diffs[n] = i + 1

# 15. 3Sum
class Solution(object):
    def threeSum(self, nums):
        res = set()
        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []

        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else: 
                z.append(num)
        
        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
	    #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))
        
        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0 ...
        if len(z) > 3:
            res.add((0,0,0))
        
        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
	    #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))
        
        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
	    #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1*(p[i]+ p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))
        
        return res

# 18. 4Sum
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.findNSum(nums, target, 4, [], res)
        return res
    
    def findNSum(self, nums, target, N, prefix, result):
       L = len(nums)
       if N == 2:
           l, r = 0, L-1
           while l < r:
               add = nums[l] + nums[r]
               if add == target:
                   result.append(prefix + [nums[l], nums[r]])
                   l += 1
                   r -= 1
                   while l<r and nums[l-1] == nums[l]:
                       l += 1
                   while l<r and nums[r+1] == nums[r]:
                       r -= 1
               elif add > target:
                   r -= 1
               else:
                   l += 1
       else:
           for i in range(L-N+1):
               if target < N*nums[i] or target > N*nums[-1]: # key judgement
                   break
               if i == 0 or (i>0 and nums[i] != nums[i-1]):
                   self.findNSum(nums[i+1:], target-nums[i], N-1, prefix+[nums[i]], result)
       return

# 11. Container With Most Water
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        areas = []
        first = 0
        last = len(height) - 1

        while first < last:
            width = last - first
            if height[first] >= height[last]: # by adding >= here instead of > we can get rid of the else condition
                area = height[last] * width
                areas.append(area)
                last -= 1
            elif height[first] < height[last]:
                area = height[first] * width
                areas.append(area)
                first += 1
            # else:
            #     area = height[first] * width 
            #     areas.append(area)
            #     last -= 1

        return max(areas)

# 1498. Number of Subsequences That Satify the Given Sum Condition
class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        c = 0
        mod = (10 ** 9 + 7)
        nums.sort()

        while i <= j:
            if nums[i] + nums[j] <= target:
                c += pow(2, (j - i), mod)   # The pow(number, power, modulus(optional)) method takes three parameters:
                                                # number- the base value that is raised to a certain power
                                                # power - the exponent value that raises number
                                                # modulus - (optional) divides the result of number paused to a power and finds the remainder: number^power% modulus
                i += 1
            else:
                j -= 1
        
        return c % mod

# 189. Rotate Array
class Solution(object):
    def reverse(self, nums, i, j):
        li = i
        ri = j

        while li < ri:
            temp = nums[li]
            nums[li] = nums[ri]
            nums[ri] = temp

            li += 1
            ri -= 1
        
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k < 0:
            k += len(nums)
        
        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

    # this solution took too long, if the k value is very large
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        while k > 0:
            nums.insert(0, nums.pop())
            k -= 1
        
        return nums