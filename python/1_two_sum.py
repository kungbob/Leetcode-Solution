################################################################################
# Question           : 1. Two Sum
# Difficulty         : Easy
# Author             : Kung Tsz Ho
# Last Modified Date : 2018/8/3
# Number of Method   : 2
# Fastest Runtime    : 36 ms
################################################################################

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
################################################################################
# Method  : 1 - double iterations
# Runtime : 5600 ms
# Beats   : 9.87 % of submissions
# Remark  :
################################################################################

        """
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                temp = nums[i] + nums[j]
                if temp == target:
                    return [i, j]

        """

################################################################################
# Method  : 2 - using dict
# Runtime : 36 ms
# Beats   : 100.00 % of submissions
# Remark  :
################################################################################

        store_dict = dict()
        for i in range(0, len(nums)):
            if (target - nums[i]) in store_dict:
                return [store_dict[target-nums[i]], i]
            store_dict[nums[i]] = i
