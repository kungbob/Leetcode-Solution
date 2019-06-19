class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        for i in range(0, len(S)):
            if S[i] in J:
                result += 1
        return result