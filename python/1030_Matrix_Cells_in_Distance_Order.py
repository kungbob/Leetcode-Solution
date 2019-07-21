class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        cellList = [(i, j) for i in range(R) for j in range(C)]
        def distance(cell):
            indexI, indexJ = cell
            return abs(indexI - r0) + abs(indexJ - c0)
        return sorted(cellList, key=distance)