// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]

var topKFrequent = function(nums, k) {
    const res = [];
    const count = {};

    for(let i = 0; i < nums.length; i++){
        if(count[nums[i]]){
            count[nums[i]] += 1
        } else {
            count[nums[i]] = 1
        }
    }

    const sorted = Object.keys(count).sort((a,b) => count[b]-count[a]);

    for(let i = 0; i < k; i++){
        res.push(sorted[i])
    }

    return res
};

// Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

// You must write an algorithm that runs in O(n) time and without using the division operation.

 

// Example 1:

// Input: nums = [1,2,3,4]
// Output: [24,12,8,6]


var productExceptSelf = function(nums) {
    const prefix = [];

    for(let i = 0; i < nums.length; i++){
        if(i===0){
            prefix[i] = 1
        } else {
            prefix[i] = nums[i - 1] * prefix[i - 1]
        }
    }

    const suffix = [];

    for(let i = nums.length -1; i >= 0; i--){
        if(i === nums.length -1){
            suffix[i] = 1
        } else {
            suffix[i] = nums[i + 1] * suffix [i + 1]
        }
    }

    const res = [];

    for(let i = 0; i < nums.length; i++){
        res[i] = prefix[i] * suffix[i]
    }

    return res
};