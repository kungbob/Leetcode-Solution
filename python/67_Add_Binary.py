class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lenA = len(a)
        lenB = len(b)
        lenLonger = max(lenA, lenB)
        result = ""
        add = 0
        for i in range(1, lenLonger + 1):
            temp = add
            if lenA - i >= 0:
                temp += int(a[-i])
            
            if lenB - i >= 0:
                temp += int(b[-i])
                
            result = str(temp % 2) + result
            add = temp // 2
        if add:
            result = "1" + result
            
        return result
            