# Normal Approach
class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for i in range(0, n - 1):
            newResult = ''
            j = 0
            while j < len(result):
                count = 1
                while j < len(result)-1 and result[j] == result[j+1]:
                    j +=  1
                    count +=  1
                j += 1
                newResult = newResult + str(count) + result[j-1]
            result = newResult
        return result 
                

# Use System Default Function
# Source: https://blog.csdn.net/coder_orz/article/details/51702322 
class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(0, n-1):
            res = ''.join([str(len(list(group))) + digit for digit, group in itertools.groupby(res)])
        return res