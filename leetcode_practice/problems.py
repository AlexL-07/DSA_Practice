# 231. Power of Two
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 2:
            return True
        
        if n % 2 != 0:
            return False
        
        temp = 2
        while temp < n:
            temp *= 2
            if temp == n:
                return True
        
        return False

# 326. Power of Three
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        if n == 1 or n == 3:
            return True
        
        temp = 3
        while temp < n:
            temp *= 3
            if temp == n:
                return True
        
        return False 

# 342. Power of Four
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1 or n == 4:
            return True
        
        if n % 4 != 0:
            return False

        temp = 4
        while temp < n:
            temp *= 4
            if n == temp:
                return True
        
        return False