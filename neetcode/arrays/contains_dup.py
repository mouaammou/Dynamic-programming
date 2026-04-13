from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for item in nums:
            if item not in seen:
                seen.add(item)
            else:
                return True
        return False

if __name__ == "__main__":
    sol = Solution()
    result = sol.containsDuplicate([1, 2, 3, 1])
    print(result)
