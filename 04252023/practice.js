// 42. Trapping Rain Water

// Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

// Example 1
// Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
// Output: 6
// Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
var trap = function(height) {
    let max1 = 0;
    //create left array so that we find the maximum element on its left...
    let left = [height.length];
    // Scan every element from left to right...
    for(let i = 0; i < height.length; i++) { 
        // Find maximum element on its left...
        if(max1 < height[i]) {
            max1 = height[i];
        }
        left[i] = max1;
    }
        
    let max2 = 0;
    //create right array so that we find the maximum element on its right...
    let right = [height.length];
    // Scan every element from right to left...
    for(let i = height.length-1; i >= 0; i--){
        // Find maximum element on its left...
        if(max2 < height[i]) {
            max2 = height[i];
        }
        right[i] = max2;
    }
        
    // To store the maximum water that can be stored..
    let trap = 0;
    // Scan and Calculate maximum trapped water...
    for(let i = 0; i  < height.length; i++) {
        trap += Math.min(left[i], right[i]) - height[i];
    }
    return trap;        //return the amount..
    
};