class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        tiles = ''.join(sorted(tiles))
        result = self.dfs(tiles, 0, 0)
        return result - 1
    
    def dfs(self, tiles, start, count):
        for i in range(start, len(tiles)):
            if i != start and tiles[i] == tiles[start]:
                continue
            tiles = self.swap(tiles, i, start)
            count = self.dfs(tiles, start + 1, count)
        count += 1
        return count
            
    def swap(self, c, i, j):
        c = list(c)
        c[i], c[j] = c[j], c[i]
        return ''.join(c)