class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for row in A:
            temp = [0] * len(row)
            for i, num in enumerate(reversed(row)):
                if num:
                    temp[i] = 0
                else:
                    temp[i] = 1
            result.append(temp)
        return result