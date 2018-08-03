################################################################################
# Question           : 8. String to Integer (atoi)
# Difficulty         : Medium
# Author             : Kung Tsz Ho
# Last Modified Date : 2018/8/3
# Number of Method   : 1
# Fastest Runtime    : 112 ms
################################################################################

################################################################################
# Method  : 1. Iterate String
# Runtime : 112 ms
# Beats   : 0 % of submissions (Too slow)
# Remark  : Need to add comments and simplify (TODO)
################################################################################
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        convert_begin = False
        result_string = ''
        for char in str:
            print(char)
            if char == ' ':
                if convert_begin:
                    break
                else:
                    continue
            elif char.isalpha() or char == '.':
                break
            elif char == '+':
                if convert_begin:
                    break
                convert_begin = True
            elif char == '-':
                if convert_begin:
                    break
                convert_begin = True
                result_string += char
            else:
                convert_begin = True
                result_string += char

        max_int = 2**31 - 1
        min_int = -2**31

        if result_string == '' or result_string == '-':
            return 0
        else:
            temp_number = float(result_string)
            if temp_number > max_int:
                return max_int
            elif temp_number < min_int:
                return min_int
            else:
                return int(result_string)
