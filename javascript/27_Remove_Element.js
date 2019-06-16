/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    var position = 0;
    for (var i = 0; i < nums.length; i++){
        if (val != nums[i]){
            
            nums[position] = nums[i]
            position += 1;
        }
    }
    return position ;
};