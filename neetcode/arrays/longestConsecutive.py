from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        n = len(nums)

        merged = [nums[0]]
        for i in range(n-1, -1, -1):
            if merged:
                if merged[-1] == nums[i] + 1:
                    merged.append(nums[i])
                else:
                    merged.pop()
            else:
                merged.append(nums[i])

        print(merged)

if __name__ == "__main__":
    sol = Solution()

    nums = [70, 20, 10, 3, 1, 2, 3, 4, 5]

    result = sol.longestConsecutive(nums)
    print(result)
        