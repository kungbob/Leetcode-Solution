class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top, front, side = 0, 0, 0
        num = len(grid)
        for i in range(num):
            x, y = 0, 0
            for j in range(num):
                if grid[i][j] != 0:
                    top += 1
                x = max(x, grid[i][j])
                y = max(y, grid[j][i])
            front += x
            side += y
        return top + front + side