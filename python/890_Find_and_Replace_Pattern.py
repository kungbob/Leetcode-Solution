class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result = []
        setPattern = set(pattern)
        
        for word in words:
            if len(set(word)) != len(setPattern):
                continue
                
            equal = True
            tempDict = dict()
            
            for i, char in enumerate(word):
                if char in tempDict:
                    if tempDict[char] != pattern[i]:
                        equal = False
                        break
                tempDict[char] = pattern[i]
                
            if equal:
                result.append(word)
                
        return result