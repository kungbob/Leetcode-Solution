class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            stones[-1] = stones[-1] - stones[-2]
            del stones[-2]
            if stones[-1] == 0:
                del stones[-1]
            stones.sort()
        if len(stones):
            return stones[0]
        else:
            return 0