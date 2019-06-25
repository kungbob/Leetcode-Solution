# Cheat
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = []
        for num in A:
            temp = num ** 2
            result.append(temp)
        return sorted(result)

# Normal Way
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        answer = collections.deque()
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
        return list(answer)