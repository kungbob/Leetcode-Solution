class Solution:
    def findNthDigit(self, n: int) -> int:
        initial = 1
        count = 9
        initialLength = 1
        while n > count * initialLength:
            n -= count * initialLength
            initialLength += 1
            initial *= 10
            count *= 10
        initial += (n - 1) / initialLength
        return int(str(initial)[(n - 1) % initialLength])