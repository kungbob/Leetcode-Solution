class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = "qwertyuiop"
        secondRow = "asdfghjkl"
        thirdRow = "zxcvbnm"
        keyboard = [firstRow, secondRow, thirdRow]
        result = []
        default = -1
        for word in words:
            tempWord = word.lower()
            if default == -1:
                for i, row in enumerate(keyboard):
                    if tempWord[0] in row:
                        default = i
            inRow = True
            for char in tempWord:
                if char not in keyboard[default]:
                    inRow = False
                    break
            if inRow:
                result.append(word)
            default = -1
        return result
            