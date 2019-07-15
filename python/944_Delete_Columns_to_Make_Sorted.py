class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        result = 0
        length = len(A[0])
        for i in range(0, length):
            column = [a[i] for a in A]
            if column != sorted(column):
                result += 1
        return result