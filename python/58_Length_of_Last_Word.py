class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s)-1, -1, -1):
            if (s[i] != ' '):
                length += 1
            else:
                if (length == 0):
                    continue
                else:
                    return length
        return length