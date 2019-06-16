/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var position = 0;
    for (var i = 0; i < nums.length; i++){
        if (nums[position] != nums[i]){
            position += 1;
            nums[position] = nums[i]
        }
    }
    return position + 1;
};