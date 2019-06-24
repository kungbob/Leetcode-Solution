class Solution:
    def toLowerCase(self, str: str) -> str:
        result = ""
        for char in str:
            if char.isupper():
                char = char.lower()
            result += char
        return result