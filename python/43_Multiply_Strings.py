class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        result = [0] * (len(num1) + len(num2))
        
        position = len(result) - 1
        
        for char1 in reversed(num1):
            temp = position
            for char2 in reversed(num2):
                multiply = (ord(char1) - ord('0')) * (ord(char2) - ord('0'))
                result[temp - 1] += (result[temp] + multiply) // 10 
                result[temp] = (result[temp] + multiply) % 10
                temp -= 1
            position -= 1
            
        start = 0
        while start < len(result) - 1 and result[start] == 0: 
            start += 1
        return ''.join(map(str, result[start:])) 
