class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) == 0:
            return []
        result = []
        for char in A[0]:
            temp = True
            for i in range(0, len(A)):
                if char not in A[i]:
                    temp = False
                    break
                else:
                    A[i] = A[i].replace(char, "", 1)
            if temp:
                result.append(char)
        return result