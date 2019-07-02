# Sample solution proved by Leetcode is wrong. Xrange(18) does not pass all test cases.
# Xrange(20) will solve the case
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        result = set()
        for i in range(0, 20):
            for j in range(0, 20):
                temp = x ** i + y ** j
                if temp <= bound:
                    result.add(temp)
                else:
                    break
        
        return list(result)