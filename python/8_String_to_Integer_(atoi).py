################################################################################
# Question           : 8. String to Integer (atoi)
# Difficulty         : Medium
# Author             : Kung Tsz Ho
# Last Modified Date : 2018/8/8
# Number of Method   : 2
# Fastest Runtime    : 56 ms
################################################################################


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

################################################################################
# Method  : 1. Iterate String
# Runtime : 112 ms
# Beats   : 0 % of submissions (Too slow)
# Remark  : Need to add comments and simplify (TODO)
################################################################################

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
        """

################################################################################
# Method  : 2. Python Strip
# Runtime : 56 ms
# Beats   : 100 % of submissions
# Remark  :
################################################################################

        result_string = ''
        max_int = 2**31 - 1
        min_int = -2**31
        positive = True

        str = str.strip()

        if not str:
            return 0

        if str[0] == '-':
            result_string += '-'
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]

        for char in str:
            if char == ' ' or char.isalpha() or char == '.' or char == '+' or char == '-':
                break
            else:
                result_string += char

        if result_string == "-" or result_string == "":
            return 0
        else:
            temp_number = float(result_string)
            if temp_number > max_int:
                return max_int
            elif temp_number < min_int:
                return min_int
            else:
                return int(result_string)
