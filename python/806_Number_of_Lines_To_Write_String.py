class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        line = 1
        remain = 0
        for char in S:
            width = widths[ord(char) - ord('a')]
            remain += width
            if remain > 100:
                line += 1
                remain = width
        return [line, remain]