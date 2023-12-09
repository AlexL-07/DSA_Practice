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

# 424. Longest Repeating Character Replacement
def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        freq = {}
        maxlen = 0
        for r in range(len(s)):
            # If a character is not in the frequency dict, this inserts it with a value of 1 (get returns 0, then we add 1).
            # If a character is in the dict, we simply add one.
            freq[s[r]] = freq.get(s[r], 0) + 1
             
            # The key point is that we only care about the MAXIMUM of the seen values.
            # Get the length of the current substring, then subtract the MAXIMUM frequency. See if this is <= K for validity.
            cur_len = r - l + 1
            if cur_len - max(freq.values()) <= k:  # if we have replaced <= K letters, record a new maxLen
                maxlen = max(maxlen, cur_len)
            else:                               # if we have replaced > K letters, then it's time to slide the window
                freq[s[l]] -= 1                 # decrement frequency of char at left pointer, then increment pointer asda45151
                l += 1
               
        return maxlen

# 567. Permutation in String
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        from collections import Counter
        window = len(s1)
        s1_c = Counter(s1) # makes a hashmap that counts the characters asdasd

        for i in range(len(s2) - window + 1):
            s2_c = Counter(s2[i:i+window])
            if s2_c == s1_c:
                return True
        
        return False
    
# 1838. Frequency of the Most Frequent Element
def maxFrequency(self, nums, k):
        maxFreq = 0
        
        # Sort the numbers first
        nums.sort()
        
        i,j = 0,0
        currSum = 0
        while j < len(nums):
            currSum += nums[j]
			# Since the array is sorted
            # The largest number for any window at any time is the current/jth element
            # So we want to know how many moves will it take to make all elements of this window = j
            # If each element becomes j, that means total sum will be nums[j] * number of elements in window
            # And we want that to be either less than or equal to sum of this window + moves we have
			# Because number of moves means how many we can add to a window so that each element is the same ...2032366565
            while nums[j] * (j - i + 1) > currSum + k: 
                currSum -= nums[i]
                i += 1
            
            # If we are here, that means, this is a valid window
            maxFreq = max(maxFreq, j - i + 1)
            j += 1
            
        return maxFreq

# 904. Fruit Into Baskets
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        ans = 0
        count = collections.defaultdict(int)

        l = 0
        for r, t in enumerate(fruits):
          count[t] += 1
          while len(count) > 2:
            count[fruits[l]] -= 1
            if count[fruits[l]] == 0:
              del count[fruits[l]]
            l += 1
          ans = max(ans, r - l + 1)

        return ans
        