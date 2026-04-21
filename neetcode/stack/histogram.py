from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 1
        n = len(heights)        
        
        for i in range(n):
            curr_min = heights[i]
            for j in range(i, n):
                curr_min = min(curr_min, heights[j])
                max_area = max(max_area, curr_min * (j - i + 1))
        return max_area

if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    sol = Solution()
    result = sol.largestRectangleArea(heights)
    print("Largest rectangle area:", result)