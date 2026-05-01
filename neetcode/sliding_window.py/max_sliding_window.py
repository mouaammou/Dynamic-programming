from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        left = 0
        for right in range(k, len(nums) + 1):
            window = nums[left: right]
            
            window.sort()
            res.append(window[-1])
            left += 1
        return res

    
nums = [1,2,1,0,4,2,6]
k = 3
print(Solution().maxSlidingWindow(nums, k))