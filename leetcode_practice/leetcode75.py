# 1768. Merge Strings Alternatively
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        if len(word1) == len(word2):
            for i in range(len(word2)):
                res += word1[i]
                res += word2[i]
        
        if len(word1) < len(word2):
            for i in range(len(word1)):
                res += word1[i]
                res += word2[i]
            res += word2[len(word1):]
        
        if len(word1) > len(word2):
            for i in range(len(word2)):
                res += word1[i]
                res += word2[i]
            res += word1[len(word2):]
        return res

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = []
        for i in range(min(len(word1), len(word2))):
            res.append(word1[i] + word2[i])
        
        return ''.join(res) + word1[i+1:] + word2[i+1:]

# 1071.Greatest Common Divisor of Strings
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        #   If concatenating str1 and str2 is not equal to concatenating str2 and str1, then there's no common divisor possible. So, we return an empty string "".
        
        if len(str1) == len(str2):
            return str1
        #   If the lengths of str1 and str2 are equal, and the concatenated strings are equal, then str1 (or str2) itself is the greatest common divisor, and we return str1 (or str2).
        
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        #   If the length of str1 is greater than the length of str2, it means that str1 contains str2 as a prefix. In this case, we recurse with the substring of str1 after removing (slicing) the prefix that matches str2.
        
        return self.gcdOfStrings(str1, str2[len(str1):])
         #   If the length of str2 is greater than the length of str1, it means that str2 contains str1 as a prefix. In this case, we recurse with the substring of str2 after removing (slicing) the prefix that matches str1.

# 1431. Kids With the Greatest Number of Candies
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandy = max(candies)
        res = []
        for n in candies:
            if n + extraCandies >= maxCandy:
                res.append(True)
            else:
                res.append(False)
        
        return res

    # cleaner solution
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxCandy = max(candies)
        res = []
        for n in candies:
            res.append(n + extraCandies >= maxCandy)
        
        return res

# 605. Can Place Flowers
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        flowerbed = [0] + flowerbed + [0]
        
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] ==0 and flowerbed[i-1] !=1 and flowerbed[i+1] !=1:
                n -= 1
                flowerbed[i] =1
                
        return n <= 0

# 345. Reverse Vowels of a String 564
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = "aeiouAEIOU"

        while start < end:
            while start < end and vowels.find(word[start]) == -1:
                start += 1
            
            while start < end and vowels.find(word[end]) == -1:
                end -= 1
            
            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1
        
        return "".join(word)

# 151. Reverse Words in a String
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        r_words = list(reversed(words))
        return " ".join(r_words)



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

# 334. Increasing Triplet Subsequence
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = float('inf') 
        second = float('inf')
            # float('inf') acts as an unbounded upper value for comparison. 
            # This is useful for finding lowest values for something 
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

# 443. String Compression
class Solution(object):

    def compress(self, chars):

        length = len(chars)

        # make it a bit faster
        if length < 2:
            return length

        # the start position of the contiguous group of characters we are currently reading.
        anchor = 0

        # position to Write Next
        # we start with 0 then increase it whenever we write to the array
        write = 0

        # we go through each caharcter till we fiand a pos where the next is not equal to it
        # then we check if it has appeared more than once using the anchor and r(read) pointers
        # 1. iterate till we find a diffrent char
        # 2. record the no. of times the current char was repeated
        for pos, char in enumerate(chars):

            # check if we have reached the end or a different char
            # check if we are end or the next char != the current
            if (pos + 1) == length or char != chars[pos+1]:
                chars[write] = char
                write += 1

                # check if char has been repeated
                # have been duplicated if the read pointer is ahead of the anchor pointer
                if pos > anchor:
                    # check no. of times char has been repeated
                    repeated_times = pos - anchor + 1

                    # write the number
                    for num in str(repeated_times):
                        chars[write] = num
                        write += 1

                # move the anchor to the next char in the iteration
                anchor = pos + 1

        return write