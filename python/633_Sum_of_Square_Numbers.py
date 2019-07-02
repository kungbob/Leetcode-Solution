class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = int(math.sqrt(c))
        while left <= right:
            tempA = left ** 2
            tempB = right ** 2
            tempR = tempA + tempB
            if (tempR == c):
                return True
            elif tempR > c:
                right -= 1
            elif tempR < c:
                left += 1
                
        return False