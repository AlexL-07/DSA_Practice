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
    