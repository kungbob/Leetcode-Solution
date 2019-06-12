/**
 * Method 1
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    var result = 0;
    for (var i = 0; i < height.length; i++) {
        for (var j = i + 1; j < height.length; j++) {
            var h = 0;
            if (height[i] > height[j]){
                h = height[j];
            }else {
                h = height[i];
            }
            
            var l = 0;
            l = j - i;
            
            var tempResult = h * l;
            if (tempResult > result) {
                result = tempResult;
            }
        }
    }
    return result;
};

/**
 * Method 2
 * Best Practice
 * Set two pointer at start & end, move the shorted height one.
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    var result = 0;
    var start = 0;
    var end = height.length - 1;

    var temp = (end - start) * Math.min(height[start], height[end]);

    while (start != end) {
        if (temp > result) {
            result = temp;
        }
        if (height[start] > height[end]){
            end -= 1;
        } else {
            start += 1;
        }
        temp = (end - start) * Math.min(height[start], height[end]);
    }

    return result;
};
