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
        new_str = ""

        for c in s:
            if c.lower() in alphabet:
                new_str += c.lower()

        return new_str == new_str[::-1]