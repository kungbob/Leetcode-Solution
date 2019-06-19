class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxR = []
        for row in grid:
            maxR.append(max(row))
            
        maxC = []
        columnLength = len(grid[0])
        for i in range(0, columnLength):
            col = self.column(grid, i)
            maxC.append(max(col))
        
        result = 0
        for i in range(0, len(grid)):
            for j in range(0, columnLength):
                result += min(maxR[i], maxC[j]) - grid[i][j]
        return result
    
    def column(self, matrix, i):
        return [row[i] for row in matrix]