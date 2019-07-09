# Source: https://blog.csdn.net/fuxuemingzhu/article/details/84206493

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        length = len(S)
        nIncrease, nDecrease = 0, length
        result = []
        for s in S:
            if s == "I":
                result.append(nIncrease)
                nIncrease += 1
            elif s == "D":
                result.append(nDecrease)
                nDecrease -= 1
        result.append(nIncrease)
        return result