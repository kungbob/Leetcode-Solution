class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x > 2**31 -1 or x < -(2**31):
            return 0

        result = ''
        if x < 0:
            result += '-'
            x *= -1
        while x % 10 == 0 and x != 0:
            x = x // 10

        temp_str = str(x)
        temp_str = temp_str[::-1]
        result += temp_str
        result = int(result)
        
        if result > 2**31 -1 or result < -(2**31):
            return 0
        return int(result)
