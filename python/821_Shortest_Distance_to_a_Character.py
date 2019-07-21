class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        if C not in S:
            return []
        result = [0] * len(S)
        start = S.index(C)
        for index, char in enumerate(S):
            if char == C:
                start = index
            result[index] = abs(index - start)
        for index in range(len(S)-1, -1, -1):
            if S[index] == C:
                start = index
            result[index] = min(abs(index - start), result[index])
        return result