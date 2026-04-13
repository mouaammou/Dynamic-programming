from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {i: None for i in nums}

        for i in range (len(nums)):
            if target - nums[i] in hash_map:
                if hash_map[nums[i]] is None:
                    hash_map[target - nums[i]] = i
                    print("ues", hash_map)
                else :
                    return [hash_map[nums[i]], i]      
        return [-1, -1]

    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     original = {value: [] for value in nums}
    #     for index in range(len(nums)):
    #         original[nums[index]].append(index)
    #     # print("orignal", original)
    #     nums.sort()
    #     left, right = 0, len(nums) - 1
    #     while (left < right):
    #         sum = nums[left] + nums[right]
    #         if sum == target:
    #             if len(original[nums[left]]) == 2:
    #                 return [original[nums[left]][0], original[nums[left]][1]]
    #             else:
    #                 return [*original[nums[left]], *original[nums[right]]]
    #         elif sum < target:
    #             left += 1
    #         else:
    #             right -= 1
    #     return [-1, -1]


if __name__ == "__main__":
    sol = Solution()
    nums = [3,6,5,4]
    target = 7

    nums=[5,5]
    target=10
    result = sol.twoSum(nums, target)
    print(result)
