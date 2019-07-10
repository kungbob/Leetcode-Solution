class Solution:
    def fib(self, N: int) -> int:
        result = self.calFib(N)
        return result
    
    def calFib(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        else:
            fib = dict()
            fib[0] = 0
            fib[1] = 1
            for i in range(2, N + 1):
                fib[i] = fib[i - 1] + fib[i - 2]
            return fib[N]
            