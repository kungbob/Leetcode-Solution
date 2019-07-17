class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        stringL = text.split()
        result = []
        indicesFirst = [i for i, x in enumerate(stringL) if x == first]
        for i in indicesFirst:
            if i < len(stringL) - 2:
                if stringL[i + 1] == second:
                    result.append(stringL[i + 2])
        return result