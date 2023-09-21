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