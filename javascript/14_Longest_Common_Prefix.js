/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    var result = "";
    if (strs.length == 0){
        return result;
    }
    for (var i = 0; i < strs[0].length; i++){
        var commonChar = strs[0][i];
        for (var j = 0; j < strs.length; j++){
            if (strs[j][i] != commonChar){
                return result;
            }
        }
        result = result.concat(commonChar);
    }
    
    return result;
};