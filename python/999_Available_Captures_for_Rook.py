class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        result = 0
        for index, row in enumerate(board):
            if 'R' in row:
                result += self.countRow(row)
                colN = row.index('R')
                rowN = index
        result += self.countCol(board, colN, rowN)
        return result
        
    def countRow(self, row):
        result = 0
        for index in range(0, len(row)):
            if row[index] == 'R':
                for i in range(index, -1, -1):
                    if row[i] == '.':
                        continue
                    elif row[i] == 'B':
                        break
                    elif row[i] == 'p':
                        result += 1
                        break
                for i in range(index, len(row)):
                    if row[i] == '.':
                        continue
                    elif row[i] == 'B':
                        break
                    elif row[i] == 'p':
                        result += 1
                        break
                break
        return result
    
    def countCol(self, board, colN, rowN):
        result = 0
        for i in range(rowN, -1, -1):
            if board[i][colN] == '.':
                continue
            elif board[i][colN] == 'B':
                break
            elif board[i][colN] == 'p':
                result += 1
                break
        for i in range(rowN, len(board)):
            if board[i][colN] == '.':
                continue
            elif board[i][colN] == 'B':
                break
            elif board[i][colN] == 'p':
                result += 1
                break
        return result