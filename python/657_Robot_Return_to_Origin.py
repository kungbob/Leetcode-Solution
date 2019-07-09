class Solution:
    def judgeCircle(self, moves: str) -> bool:
        xAxis = 0
        yAxis = 0
        for move in moves:
            if move == 'U':
                yAxis += 1
            elif move == 'D':
                yAxis -= 1
            elif move == 'R':
                xAxis += 1
            elif move == 'L':
                xAxis -= 1
        if xAxis == 0 and yAxis == 0:
            return True
        else:
            return False