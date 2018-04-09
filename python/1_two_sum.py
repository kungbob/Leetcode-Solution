class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        # Method 1, double iterations
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                temp = nums[i] + nums[j]
                if temp == target:
                    return [i, j]

        """

        # Method 2, using dict
        store_dict = dict()
        for i in range(0, len(nums)):
            if (target - nums[i]) in store_dict:
                return [store_dict[target-nums[i]], i]
            store_dict[nums[i]] = i
