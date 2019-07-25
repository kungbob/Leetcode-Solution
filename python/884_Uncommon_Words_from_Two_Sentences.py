class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        result = []
        AList = A.split(' ')
        BList = B.split(' ')
        ACount = collections.Counter(AList)
        for key, value in ACount.items():
            if value > 1:
                continue
            if key in BList:
                continue
            result.append(key)
        BCount = collections.Counter(BList)
        for key, value in BCount.items():
            if value > 1:
                continue
            if key in AList:
                continue
            result.append(key)
        return result