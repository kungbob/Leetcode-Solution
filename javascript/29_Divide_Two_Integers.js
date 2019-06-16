/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    
    const MAX_VALUE=Math.pow(2,31)-1;
    const MIN_VALUE=Math.pow(-2,31);
    
    var sign = 1;
    if(Math.sign(dividend) != Math.sign(divisor) ){
        sign = -1;
    }
    
    var absDividend = Math.abs(dividend);
    var absDivisor = Math.abs(divisor);
    
    if(absDivisor == 0){
        return MAX_VALUE;
    } 
    
    if( absDividend == 0 || absDividend < absDivisor){
       return 0; 
    } 

    var result = division(absDividend, absDivisor);


    if(result>MAX_VALUE){
        result = (sign==1) ? MAX_VALUE:MIN_VALUE;
    } else {
        result *= sign;
    }

    return result;
};

var division = function(absDividend,absDivisor){
    if(absDividend < absDivisor){
        return 0;
    } 

    var sum = absDivisor;
    var multiple = 1;
    while((sum + sum) <= absDividend){
        sum += sum;
        multiple += multiple;
    }
    return multiple + division(absDividend - sum, absDivisor)
};

/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    
    const MAX_VALUE=Math.pow(2,31)-1;
    const MIN_VALUE=Math.pow(-2,31);
    
    var sign = 1;
    if(Math.sign(dividend) != Math.sign(divisor) ){
        sign = -1;
    }
    
    var absDividend = Math.abs(dividend);
    var absDivisor = Math.abs(divisor);
    
    if( absDivisor == 0){
        return MAX_VALUE;
    } 
    
    if( absDividend == 0 || absDividend < absDivisor){
       return 0; 
    } 
    
    var result = 0;

    while (absDividend >= absDivisor) {
        var temp = absDivisor;
        var i = 0;
        var tempDivisor = temp << 1;
        while (absDividend >= tempDivisor) {
            if ((tempDivisor) <= 0) {
                break;
            }
            temp = temp << 1;
            tempDivisor = temp << 1;
            i++;
            if (sign > 0 && i > 29) {
                return MAX_VALUE;
            }
            if (sign < 0 && i > 30) {
                return MIN_VALUE;
            }
        }
        absDividend -= temp;
        result += Math.pow(2, i);
    }


    if(result>MAX_VALUE){
        result = (sign==1) ? MAX_VALUE:MIN_VALUE;
    } else {
        result *= sign;
    }

    return result;
};


/**
 * TLE Approach : Use Minus
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    
    const MAX_VALUE=Math.pow(2,31)-1;
    const MIN_VALUE=Math.pow(-2,31);
    
    if (dividend == 0){
        return 0;
    }
    var result = 0;
    
    var absDividend = Math.abs(dividend);
    var absDivisor = Math.abs(divisor);
    
    
    if (dividend > MAX_VALUE){
        return MAX_VALUE;
    } else if (dividend < MIN_VALUE) {
        return MIN_VALUE;
    } else {
        while (absDividend >= absDivisor) {
            absDividend -= absDivisor
            result += 1
        }
    }
    
    if (Math.sign(dividend) != Math.sign(divisor) ){
        result =  0 - result;
    }
    
    if (result > MAX_VALUE) {
        return MAX_VALUE;
    } else if (result < MIN_VALUE) {
        return MIN_VALUE;
    }
    
    return result
};