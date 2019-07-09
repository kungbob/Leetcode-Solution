class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right + 1):
            temp = i
            selfDivide = True
            while temp:
                div = temp % 10
                if not div or i % div != 0:
                    selfDivide = False
                    break
                temp = temp // 10
            if selfDivide:
                result.append(i)
        return result