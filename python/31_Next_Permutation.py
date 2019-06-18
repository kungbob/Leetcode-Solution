class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end = len(nums) - 1
        while end != 0:
            if nums[end] > nums[end - 1]:
                break
            end -= 1
        
        if end == 0:
            return nums.sort()
        
        for i, num in reversed(list(enumerate(nums))):
            if nums[i] > nums[end - 1]:
                nums[i], nums[end - 1] = nums[end - 1], nums[i]
                break
        last = len(nums)
        nums[end:] = [nums[i] for i in range(last-1, end-1, -1)]