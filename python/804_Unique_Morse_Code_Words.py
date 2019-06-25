class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        newWords = []
        for word in words:
            tempMorse = ""
            for char in word:
                newChar = morse[ord(char) - ord('a')]
                tempMorse += newChar
            newWords.append(tempMorse)
        return len(set(newWords))