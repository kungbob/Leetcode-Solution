class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        modifyPos = 0
        temp = chars[0]
        count = 0
        for countPos in range(0, len(chars)):
            if temp != chars[countPos]:
                chars[modifyPos] = temp
                modifyPos += 1
                if count > 1:
                    tempStr = str(count)
                    for char in tempStr:
                        chars[modifyPos] = char
                        modifyPos += 1
                count = 1
                temp = chars[countPos]
            else:
                count += 1
            
        chars[modifyPos] = temp
        modifyPos += 1
        if count > 1:
            tempStr = str(count)
            for char in tempStr:
                chars[modifyPos] = char
                modifyPos += 1
        if modifyPos <= countPos:
            del chars[modifyPos:]
                
        return len(chars)