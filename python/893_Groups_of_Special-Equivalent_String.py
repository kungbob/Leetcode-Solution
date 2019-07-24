# Source: https://blog.csdn.net/fuxuemingzhu/article/details/82083609

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        result = set()
        for string in A:
            result.add(''.join(sorted(string[0::2])) + ''.join(sorted(string[1::2])))
        return len(result)