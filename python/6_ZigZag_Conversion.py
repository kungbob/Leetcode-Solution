class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        length = len(s)
        result = ''

        if numRows == 1:
            return s


        for i in range(numRows):
            line_start = i
            while line_start < length:
                result += s[line_start]
                # Handle the first line and middle line
                if not (i == numRows - 1):
                    line_start += (numRows-1-i) * 2
                else:
                    # Handle the last line
                    line_start += i * 2
                # Handle the middle line
                if (line_start >= length) or (i == 0)  :
                    continue
                else:
                    result += s[line_start]
                    line_start += i * 2

        return result
