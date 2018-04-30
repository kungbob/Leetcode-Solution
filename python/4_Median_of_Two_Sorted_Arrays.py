class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2);
        if total % 2 == 0 :
            return (self.findMedian(nums1, nums2, total // 2 ) + self.findMedian(nums1, nums2, total // 2 + 1 ) ) / 2
        else:
            return self.findMedian(nums1, nums2, total // 2 + 1)

    def findMedian(self, num1, num2, k):

        if len(num1) < len(num2):
            return self.findMedian(num2, num1, k)

        if len(num2) == 0:
            return num1[k - 1]

        if k == 1:
            return min(num1[0], num2[0])

        middle_num2 = min(k // 2, len(num2))
        middle_num1 = k - middle_num2

        if num1[middle_num1 - 1] >= num2[middle_num2 - 1]:
            return self.findMedian(num1, num2[middle_num2:], middle_num1)
        else:
            return self.findMedian(num1[middle_num1:], num2, middle_num2)
