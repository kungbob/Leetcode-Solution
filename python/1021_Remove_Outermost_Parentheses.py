class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        previous = 0
        count = 0
        result = ""
        for i, char in enumerate(S):
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            
            if count == 0:
                result += S[previous + 1 : i]
                previous = i + 1
                
        return result