// Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

// You must write an algorithm that runs in O(n) time.

 

// Example 1:

// Input: nums = [100,4,200,1,3,2]
// Output: 4
// Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


var longestConsecutive = function(nums) {
    let set = new Set(nums);

    let maxCount = 0   
    for(let ele of nums){  
        if(!set.has(ele-1)){  
            let count = 0  
            while(set.has(ele)){  
                ele++   
                count++  
            }
            maxCount = Math.max(maxCount, count)  
        }
    }
    return maxCount
    
}