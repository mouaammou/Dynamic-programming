from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n - 1
        water = 0

        leftmax = [0] * n
        rightmax = [0] * n

        leftmax[0] = height[0]
        for i in range (1, n):
           leftmax[i] = max(leftmax[i - 1], height[i])


        rightmax[-1] = height[-1]
        for i in range(n-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], height[i])

        for i in range(n):
            water += min(leftmax[i], rightmax[i]) - height[i]

        return water
    

    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = 0
        right = n - 1
        water = 0

        r_max = height[right]
        l_max = height[left]

        while left < right:
            if l_max < r_max:
                left += 1
                l_max = max(l_max, height[left])
                water += l_max - height[left]
            else:
                right -= 1
                r_max = max(r_max, height[right])
                water += r_max - height[right]

        return water


sol = Solution()
print(sol.trap([0,2,0,3,1,0,1,3,2,1]))  # Expected output: 6
            
            


