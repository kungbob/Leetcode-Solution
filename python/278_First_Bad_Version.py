# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n
        
        while end >= start:
            middle = (start + end) // 2 
            if isBadVersion(middle):
                if end == start:
                    return end
                else:
                    end = middle
            else:
                start = middle + 1
        return 0