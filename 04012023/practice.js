// Given an array of strings strs, group the anagrams together. You can return the answer in any order.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


var groupAnagrams = function(strs) {
    const hash = {};

    for(let i = 0; i < strs.length; i++){
        const newString = strs[i].split("").sort().join("");
        if(hash[newString]){
            hash[newString].push(strs[i]);
        } else {
            hash[newString] = [strs[i]]
        };
    };
    return Object.values(hash)
};