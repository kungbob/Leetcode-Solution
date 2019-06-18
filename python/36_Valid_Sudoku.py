class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result = True
        
        # Check row
        for row in board:
            setOfRow = set([x for x in row if row.count(x) > 1])
            # Should contain '.' only
            if (len(setOfRow) > 1):
                result = False
                return result
        
        # Check column
        for i in range(0, 9):
            column = [row[i] for row in board]
            setOfColumn = set([x for x in column if column.count(x) > 1])
            if (len(setOfColumn) > 1):
                result = False
                return result
            
        # Check Block
        for i in range(0, 3):
            for j in range(0, 3):
                startRow = i * 3
                startColumn = j * 3
                rows = board[startRow:startRow+3]
                nums = [row[startColumn:startColumn + 3] for row in rows]
                # Flatten
                flattenNums = []
                for sublist in nums:
                    for item in sublist:
                        flattenNums.append(item)
                setOfNums = set([x for x in flattenNums if flattenNums.count(x) > 1])
                if (len(setOfNums) > 1):
                    result = False
                    return result

        return result