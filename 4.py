## 4. Median of Two Sorted Arrays

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        sortedNums = sorted(nums1 + nums2)
        
        if len(sortedNums) % 2 == 0:
            return (sortedNums[(len(sortedNums) / 2) - 1] +  sortedNums[len(sortedNums) / 2]) / 2.0
        return sortedNums[len(sortedNums) / 2]

