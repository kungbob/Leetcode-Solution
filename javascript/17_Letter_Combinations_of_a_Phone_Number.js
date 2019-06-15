/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    var two = ['a', 'b', 'c'];
    var three = ['d', 'e', 'f'];
    var four = ['g', 'h', 'i'];
    var five = ['j', 'k', 'l'];
    var six = ['m', 'n', 'o'];
    var seven = ['p', 'q', 'r', 's'];
    var eight = ['t', 'u', 'v'];
    var nine = ['w', 'x', 'y', 'z'];
    
    var telephone = {
        '2': two,
        '3': three,
        '4': four,
        '5': five,
        '6': six,
        '7': seven,
        '8': eight,
        '9': nine
    };
    
    var result = [];
    
    for (var i = 0; i < digits.length; i++){
        var charList = telephone[digits[i]];
        var tempList = []
        
        for (var j = 0; j < charList.length; j++){
            var char = charList[j];
            
            if (result.length == 0) {
                tempList = charList;
            } else {
                for (var k = 0; k < result.length; k++){
                    tempList.push(result[k] + char);
                }
            }
        }
        result = tempList;
    }
    return result;
};