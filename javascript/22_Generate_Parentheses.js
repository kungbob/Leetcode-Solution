/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    var result = [];
    dfs(n, n, "", result);
    return result;
};

var dfs = function(left, right, string, result) {
    if (left == 0 && right == 0){
        result.push(string);
        return;
    }
    
    if (left > 0 ) {
        dfs(left-1, right, string + "(", result);
    }  
    if (right > left ){
        dfs(left, right-1, string + ")", result);
    } 
}