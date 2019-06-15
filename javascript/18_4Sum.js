/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target) {
    nums.sort(function(a, b) {
      return a - b;
    });
    
    var result = [];
    for (var i = 0; i < nums.length - 3; ++i){
        if (i > 0 && nums[i] == nums[i-1]){
            continue;
        }
        
        var j = i + 1;
        
        for (; j < nums.length - 2; ++j){
            if (j > i + 1 && nums[j] == nums[j-1]){
                continue;
            }
            
            var start = j + 1;
            var end = nums.length - 1;
            var newtarget = target - nums[i] - nums[j];
            
            while (end > start) {
                if (nums[start] + nums[end] == newtarget){
                    result.push([nums[i], nums[j], nums[start], nums[end]]);
                    
                    // Move pointer to avoid duplicate
                    while (end > start && nums[start] == nums[start + 1]){
                        start += 1;
                    }
                    
                    while (end > start && nums[end] == nums[end - 1]){
                        end -= 1;
                    }
                    start += 1;
                    end -= 1;
                } else if (nums[end] + nums[start] < newtarget) {
                    start += 1;
                } else {
                    end -= 1;
                }
            }
        }
    }
    return result;
};