# Slow Approach
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if (len(nums) == 0):
            return [-1, -1]
        
        start = 0
        end = len(nums) - 1
        
        if nums[start] > target or nums[end] < target:
            return [-1, -1]
        else:
            while start <= end:
                half = (start + end ) // 2
                if nums[half] == target:
                    end = half
                    start = half
                    while start - 1 >= 0 and nums[start - 1] == target:
                        start -= 1
                    while end < len(nums) - 1 and nums[end + 1] == target:
                        end += 1
                    return [start, end]
                elif nums[half] < target:
                    start = half + 1
                else:
                    end = half - 1
        
        return [-1, -1]

# Fast Approach
# Learned from: https://blog.csdn.net/fuxuemingzhu/article/details/83273084
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.lowwer_bound(nums, target)
        right = self.higher_bound(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]
    
    def lowwer_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    
    def higher_bound(self, nums, target):
        # find in range [left, right)
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left