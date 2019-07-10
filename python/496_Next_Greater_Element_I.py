class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapNum = dict()
        result = [-1] * len(nums1)
        for i in range(0, len(nums2)):
            mapNum[nums2[i]] = i
            
        for i in range(0, len(nums1)):
            start = mapNum[nums1[i]]
            for j in range(start + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    result[i] = nums2[j]
                    break
        return result