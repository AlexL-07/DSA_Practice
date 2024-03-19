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

# 258. Add Digits
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = (num % 10) + (num // 10)
        
        return num

# 70. Climbing Stairs
    # using the pull dynamic programing(DP) technique
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        step1 = 1
        step2 = 2
        x = 0
        for i in range(2, n):
            x = step1 + step2
            step1 = step2
            step2 = x
        
        return x