/**
 * Slow Approach
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    var result = -1;
    var previous = false;
    
    if (needle.length == 0){
        return 0;
    }
    
    for (var i = 0; i < haystack.length; i++){
        var found = true;
        var start = i;
        if (!previous){
            for (var j = 0; j < needle.length; j++){
                if (haystack[start] == needle[j]){
                    start += 1;
                    continue;
                }else {
                    found = false;
                }
            }
        }
        
        if (found){
            result = i;
            return result;
        }
    }
    
    return result;
};

/**
 * Cheat
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    return haystack.indexOf(needle);
};

/**
 * Improve of first approach
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    if (needle.length == 0) {
        return 0;
    }

    var result = -1;
    if (needle.length > haystack.length){
        return result;
    }

    for (var i = 0; i < haystack.length; i++){
        var compareStr = haystack.substr(i, needle.length);
        if (compareStr == needle) {
            return i;
        }
    }

    return -1;
};