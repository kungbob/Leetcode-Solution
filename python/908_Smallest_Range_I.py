class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        maxN = max(A)
        minN = min(A)
        return max(maxN - minN - 2 * K, 0)