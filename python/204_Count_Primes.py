class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primeList = [1] * n
        primeList[0] = 0
        primeList[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if primeList[i]:
                for j in range(i * 2, n, i):
                    primeList[j] = 0
        return sum(primeList)