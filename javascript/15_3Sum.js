/**
 * Best Practice
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort(function(a, b) {
      return a - b;
    });
    var result = [];
    for(var i = 0; i < nums.length -2; ++i) {
        if (nums[i] > 0){
            break;
        }
        if (i > 0 && nums[i] == nums[i-1]){
            continue;
        }
        
        // Set two pointers from start & end
        var start = i + 1;
        var end = nums.length - 1;
        var target = 0 - nums[i];
        
        while (end > start){
            if (nums[start] + nums[end] === target){
                result.push([nums[i], nums[start], nums[end]]);
                
                // Move pointer to avoid duplicate
                while (end > start && nums[start] == nums[start+1]){
                    start += 1;
                }
                while (end > start && nums[end] == nums[end-1]){
                    end -= 1;
                }
                start += 1;
                end -= 1;
            } else if (nums[end] + nums[start] < target) {
                start += 1;
            } else {
                end -= 1;
            }
           
        }
    }
    return result;
};