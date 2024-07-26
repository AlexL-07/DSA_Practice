# 1768. Merge Strings Alternatively
from collections import defaultdict
# have to import defaultdict to use it here I guess


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

# 392. Is Subsequence
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0 
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)

# 11. Container With Most Water
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        areas = []
        f = 0
        l = len(height) - 1

        while f <= l:
            w = l - f
            if height[f] >= height[l]:
                area = w * height[l]
                areas.append(area)
                l -= 1
            elif height[f] < height[l]:
                area = w * height[f]
                areas.append(area)
                f += 1

        return max(areas) 

# 1679. Max Number of K-Sum Pairs
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        f = 0
        n = len(nums) - 1
        sort_nums = sorted(nums)

        while f < n:
            if sort_nums[f] + sort_nums[n] == k:
                count += 1
                f += 1
                n -= 1
            elif sort_nums[f] + sort_nums[n] > k:
                n -= 1
            elif sort_nums[f] + sort_nums[n] < k:
                f += 1
        
        return count 

# 643. Maximum Average Subarray I
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        maxSum = windowSum = float(sum(nums[:k]))
        # gets the first windowSum and sets the maxSum to this first windowSum

        for i in range(k, len(nums)):
            windowSum += nums[i] 
            # adds in the number following the last number from the initial window sum
            windowSum -= nums[i - k]
            # subtracts the first number from the initial and subsequent window sums
            maxSum = max(windowSum, maxSum)
            # compares and sets the maxSum by comparing the current windowSum to the running maxSum

        return maxSum/k

# 456. Maximum Number of Vowels in a Substring of Given Length
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        f = 0
        n = k
        maxLength = 0

        while n <= len(s):
            sub = s[f:n]
            count = sum(sub.count(vowel) for vowel in vowels)
            maxLength = max(count, maxLength)
            f += 1
            n += 1
        
        
        return maxLength

    # WAY MORE EFFICIENT SOLUTION 100x
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = set('aeiou')
        currCount = 0

        for i in range(k):
            if s[i] in vowels:
                currCount += 1
        
        res = currCount

        for i in range(k, len(s)):
            if s[i] in vowels:
                currCount += 1
            if s[i-k] in vowels:
                currCount -= 1
            res = max(res, currCount)

        return res

# 1004. Max Consecutive Ones III
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = 0
        e = 0
        r = 0
        zero_count = 0

        while e < len(nums):
            if nums[e] == 1:
                e += 1
                r = max(r, e - s)
            else:
                if zero_count < k:
                    e += 1
                    zero_count += 1
                    r = max(r, e - s)
                else:
                    while s <= e and zero_count >= k:
                        if nums[s] == 0:
                            zero_count -= 1
                        s += 1
        
        return r

# 1493. Longest Subarray of 1's After Deleting One Element
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 not in nums:
            return len(nums) - 1
        
        s = 0
        e = 0
        r = 0
        z_count = 0

        while e < len(nums):
            if nums[e] == 1:
                e += 1
                r = max(r, e - s)
            else:
                if z_count == 0:
                    z_count += 1
                    e += 1
                    r = max(r, e - s)
                else:
                    while s <= e and z_count > 0:
                        if nums[s] == 0:
                            z_count -= 1
                        s += 1
        
        return r - 1 

# 1732. Find the Highest Altitude
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alts = [0]

        for g in gain:
            new_alt = alts[-1] + g
            alts.append(new_alt)
        
        return max(alts)

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt = 0
        max_alt = 0

        for g in gain:
            alt += g
            max_alt = max(alt, max_alt)
        
        return max_alt

# 724. Find Pivot Index
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum = 0
        rightSum = sum(nums)

        for i, n in enumerate(nums):
            rightSum -= n
            if leftSum == rightSum:
                return i
            leftSum += n
        
        return -1 

# 2215. Find the Difference of Two Arrays
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        return [set(nums1) - set(nums2), set(nums2) - set(nums1)]

# 1207. Unique Number of Occurences
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = {}

        for n in arr:
            count[n] = count.get(n, 0) + 1

        unique = []
        
        for v in count.values():
            if v in unique:
                return False
            unique.append(v)
        
        return True

# 1657. Determine if Two Strings Are Close
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        hash1 = {}
        hash2 = {}

        for w in word1:
            hash1[w] = hash1.get(w, 0) + 1

        for w in word2:
            hash2[w] = hash2.get(w, 0) + 1
        

        return sorted(hash1.keys()) == sorted(hash2.keys()) and sorted(hash1.values()) == sorted(hash2.values())

# 2352. Equal Row and Column Pairs
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        hashMap = defaultdict(int)
            # sets the default value to zero for a hashmap when initialized using defaultdict(int)

        for row in grid:
            rowStr = str(row)
            hashMap[rowStr] += 1
        
        count = 0
        for j in range(n):
            col = [grid[i][j] for i in range(n)]
            colStr = str(col)
            count += hashMap[colStr]
        
        return count

# 2390. Remove Stars From a String
class Solution(object):
    def removeStars(self, s):
        stack = []

        # Iterate over each character in the input string
        for c in s:
            # If the current character is a star and the stack is not empty, pop the topmost character
            # from the stack
            if c == '*' and stack:
                stack.pop()
            # Otherwise, push the current character onto the stack
            else:
                stack.append(c)

        # Convert the stack to a string and return it as the output
        return ''.join(stack)

    # Same concept but faster
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []

        for c in s:
            if c != '*':
                stack.append(c)
            elif stack:
                stack.pop()
        
        return ''.join(stack)

# 735. Asteroid Collision
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 > a:
                if stack[-1] + a < 0:
                    stack.pop()
                elif stack[-1] + a > 0:
                    break
                else: # when stack[-1] == a
                    stack.pop()
                    break
            else:
                stack.append(a)
        
        return stack

# 394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        # Initialize the stack and the current string
        stack = []
        curr_str = ""
        # Initialize the current number to 0
        curr_num = 0
        
        # Iterate through each character of the string
        for c in s:
            # If the character is a digit, update the current number
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            # If the character is an opening bracket, push the current number and current string onto the stack
            elif c == "[":
                stack.append(curr_num)
                stack.append(curr_str)
                # Reset the current number and current string
                curr_num = 0
                curr_str = ""
            # If the character is a closing bracket, repeat the popped characters and push the result back onto the stack
            elif c == "]":
                prev_str = stack.pop()
                prev_num = stack.pop()
                curr_str = prev_str + curr_str * prev_num
            # If the character is a letter, append it to the current string
            else:
                curr_str += c
        
        # Pop any remaining characters from the stack and concatenate them to the final result
        while stack:
            curr_str = stack.pop() + curr_str
        
        return curr_str

# 933. Number of Recent Calls
from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.q = deque()
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.q.append(t)

        while t - self.q[0] > 3000:
            self.q.popleft()
        
        return len(self.q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# 649. Dota2 Senate
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        # Senator in Radiant
        R_queue = deque(i for i, x in enumerate(senate) if x == 'R')
        # Senator in Dire
        D_queue = deque(i for i, x in enumerate(senate) if x == 'D')
        
        # Keep playing if both sides still have senator
        while R_queue and D_queue:
            r = R_queue.popleft()
            d = D_queue.popleft()

            if r < d:
                # First Radiant bans another one in Dire
                # Radiant wins at this round
                R_queue.append(r + n)
            else:
                # First Dire bans another one in Radiant
                # Dire wins at this round
                D_queue.append(d + n)
        

        if R_queue:
            # Finally, Radiant declares victory.
            # Dire lost all senators.
            return 'Radiant'
        else:
            # Finally, Dire declares victory.
            # Radiant lost all senators.
            return 'Dire'

# 2095. Delete the Middle Node of a Linked List
class ListNode(object):
    # this class was given with the problem
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if head is None:
            return None
        # If head is null, the list is empty. The method returns null since there's nothing to delete.
        
        prev = ListNode(0)
        prev.next = head
        slow = prev
        fast = head
        # A dummy node, prev, is created and its next pointer is set to head. This dummy node serves as a placeholder to simplify edge case handling, especially when the list has only one node or when we need to delete the first real node of the list.
        # Two pointers, slow and fast, are initialized: slow starts at prev and fast starts at head.

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            # The list is traversed using the two-pointer technique where fast moves twice as fast as slow. For every move fast makes two steps (if possible), slow makes one step.
            # This traversal continues until fast reaches the end of the list (fast is null) or fast is at the last node (fast.next is null). At this point, slow will be just before the middle node of the list. This is because while fast moves through the entire list, slow moves only half the distance.

        slow.next = slow.next.next
        # Once the traversal is complete, slow is either at the node just before the middle of the list (for odd-length lists) or at the node before the second middle node (for even-length lists, where there are two middle nodes, and the first one is considered the middle for deletion).
        # The middle node is then removed by adjusting the next pointer of the slow node to skip over the middle node and point directly to the node after the middle node. This effectively removes the middle node from the list.
        return prev.next
        # Finally, the method returns the new list, but since the prev node was a dummy node added at the start, the method returns prev.next to return the actual head of the modified list. 

# 328. Odd Even Linked List
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head
        # Base Case Handling: The code first checks if the input list is either empty (head == null) or contains only one node (head.next == null). 
            # In either case, the list doesn't need rearranging, so the original head of the list is returned immediately.
        
        odd = ListNode(0)
        even = ListNode(0)
        # Dummy Head Initialization: Two dummy head nodes, odd and even, are created. 
            # These nodes serve as the starting points for two separate lists: one to collect all nodes from odd positions and the other for nodes from even positions. 
            # This is a common technique used to simplify list manipulation by avoiding dealing with special cases for the head node.
        odd_ptr = odd
        even_ptr = even
        # Pointer Initialization: Two pointers, odd_ptr and even_ptr, are initialized to point to the respective dummy heads. 
            # These pointers will traverse the lists, allowing new nodes to be appended to the respective odd and even lists.
        idx = 1
        # This variable is used to determine whether the current node is at an odd or even position

        while head != None:
            # List Traversal and Node Classification: The code enters a loop that continues until all nodes from the original list (head) have been processed. 
                # Within the loop, an index variable is used to determine whether the current node is at an odd or even position:
            if idx % 2 != 0:
                # If index is odd, the current node belongs to the odd list, so it's appended to the list that odd_ptr is building. 
                # odd_ptr is then advanced to this newly added node.
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
            else:
                # If index is even, a similar process is followed for the even list using even_ptr.
                even_ptr.next = head
                even_ptr = even_ptr.next
                
            head = head.next
            idx += 1
        
        even_ptr.next = None
        odd_ptr.next = even.next
        # Linking Odd and Even Lists: After all nodes have been classified and the original list has been fully traversed, the code performs two crucial steps to finalize the rearrangement:
            # The end of the even list is marked by setting even_ptr.next to null. 
                # This ensures the even list is properly terminated and doesn't inadvertently link back to any nodes that might follow it in memory.
            # The odd and even lists are concatenated. 
                # This is done by setting the next pointer of the last node in the odd list (odd_ptr.next) to point to the first real node in the even list (even.next), effectively skipping the even dummy head.
        return odd.next
        # Returning the Result: Finally, the method returns odd.next, which points to the first real node in the odd list, effectively skipping the odd dummy head. 
            # This is the new head of the rearranged list where all odd-positioned nodes are followed by all even-positioned nodes.

# 206. Reverse Linked List
class Solution(object):
    def reverseList(self, head):
        # Initialize prev pointer as NULL...
        prev = None
        # Initialize the curr pointer as the head...
        curr = head
        # Run a loop till curr points to NULL...
        while curr:
            # Initialize next pointer as the next pointer of curr...
            next = curr.next
            # Now assign the prev pointer to curr’s next pointer.
            curr.next = prev
            # Assign curr to prev, next to curr...
            prev = curr
            curr = next
        return prev       # Return the prev pointer to get the reverse linked list...

# 2130. Maximum Twin Sum of a Linked List
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        
        N = len(nums)
        res = 0
        for i in range(N // 2):
                # // is floor division in python 
            res = max(res, nums[i] + nums[N - i - 1])
        
        return res

# 104. Maximum Depth of Binary Tree
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# recursive solution 
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
# iterative solution 
import collections
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        deque = collections.deque()
        depth = 0

        if root:
            deque.append(root)
        
        while deque:
            size = len(deque)
            for _ in range(size):
                node = deque.popleft()
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            depth += 1
        
        return depth
    
        


