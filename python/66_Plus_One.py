class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lastDigit = digits[-1]
        if lastDigit != 9:
            digits[-1] = lastDigit + 1
            return digits
        else:
            add = True
            position = -1
            digits[-1] = 0
            for i in range(len(digits) - 2, -1, -1):
                if digits[i] != 9:
                    digits[i] = digits[i] + 1
                    add = False
                    return digits
                else:
                    digits[i] = 0
            if add:
                digits.insert(0, 1)
        
        return digits
            
                    