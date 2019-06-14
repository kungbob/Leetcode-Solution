/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    nums.sort(function(a, b) {
      return a - b;
    });
    
    var result = nums[0] + nums[1] + nums[2];
    var minDist = Math.abs(target - result);
    
    for(var i = 0; i < nums.length -2; ++i) {
        if (i > 0 && nums[i] == nums[i-1]){
            continue;
        }
        
        // Set two pointers from start & end
        var start = i + 1;
        var end = nums.length - 1;
        var tempTarget = target - nums[i];
        
        while (end > start) {
            var tempSum = nums[start] + nums[end];
            if (tempSum == tempTarget){
                return target;
            }
            
            var tempDist = Math.abs(tempTarget - nums[start] - nums[end]);
            
            if (tempDist < minDist) {
                minDist = tempDist;
                result = tempSum + nums[i];
            }
            
            if (tempSum < tempTarget){
                start += 1;
            } else {
                end -= 1;
            }
            
        }
        
        
    }
    return result;
    
};