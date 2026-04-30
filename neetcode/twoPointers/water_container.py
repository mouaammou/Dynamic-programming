from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        n = len(heights)
        max_water = 0
        left = 0
        right = n - 1

        while left < right:
            dis = right - left 
        
            if heights[left] > heights[right]:
                max_water = max(max_water, dis * heights[right])
                right -= 1
            else:
                max_water = max(max_water, dis * heights[left])
                left += 1
            
        return (max_water)

input = [2,2,2]
print(Solution().maxArea(input))