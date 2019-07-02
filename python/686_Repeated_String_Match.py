class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        result = A
        repeat = 1
        while len(result) < len(B):
            result += A
            repeat += 1
        
        if result.find(B) != -1:
            return repeat
        else:
            result += A
            repeat += 1
            if result.find(B) != -1:
                return repeat
            
        return -1
            