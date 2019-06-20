# Source: https://blog.csdn.net/fuxuemingzhu/article/details/79431941
class Solution:
    def countArrangement(self, N: int) -> int:
        visited = [0] * (N + 1)
        result = self.countBeauty(N, 1, visited)
        return result
    
    def countBeauty(self, num, index, visited):
        if index > num :
            return 1
        
        total = 0
        for i in range(1, num  + 1):
            if visited[i] != 1 and (i % index == 0 or index % i == 0):
                visited[i] = 1
                total += self.countBeauty(num, index + 1, visited)
                visited[i] = 0
        return total