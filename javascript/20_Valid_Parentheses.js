/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    var stack = [];
    for (var i = 0; i < s.length; i++){
        var char = s[i];
        if (char == '(' || char == '{' || char == '['){
            stack.push(char)
        } else {
            
            var previous = stack.pop();
            if (char == ')' && previous == '('){
                continue;
            }else if (char == '}' && previous == '{'){
                continue;
            }else if (char == ']' && previous == '['){
                continue;
            }else {
                return false;
            }
        }
    }
    if (stack.length > 0) {
        return false;
    } else {
        return true;
    }
};