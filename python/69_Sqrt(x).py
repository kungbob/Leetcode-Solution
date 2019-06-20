# Newton's method
class Solution:
    def mySqrt(self, x: int) -> int:
        if (x == 0):
            return 0
        result = x
        while (result * result > x ):
            result = (result + x // result) // 2
        return int(result)