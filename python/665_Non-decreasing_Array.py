class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        if len(nums) == 0 or len(nums) == 1:
            return True
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
            if count > 1:
                return False
        return True