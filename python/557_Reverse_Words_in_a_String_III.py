class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        stringList = s.split(' ')
        for substring in stringList:
            substring = substring[::-1]
            result += substring + " "
        return result[:-1]