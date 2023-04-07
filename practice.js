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