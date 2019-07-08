class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortHeight = sorted(heights)
        count = 0
        for i in range(0, len(heights)):
            if sortHeight[i] != heights[i]:
                count += 1
        return count