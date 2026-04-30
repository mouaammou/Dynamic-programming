from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        # median for odd is the middle
        # medain for even is middle-1 and middle

        if len(merged) % 2 == 0:
            mid = (len(merged) - 1) // 2
            mid_1 = mid - 1
            if mid_1 >= 0:
                return float (merged[mid] + merged[mid_1]) / 2
        else:
            return merged[(len(merged) - 1) // 2]


nums1 = [1,2]
nums2 = [3, 4]

solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))