from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        for i in range(len(nums)):
            j = 0
            res = 1
            while j < len(nums):
                if j != i:
                    res *= nums[j]
                    # print(nums[j])
                j+= 1
            print("ss")
            output.append(res)
        print(output)

    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 1, 1
        n = len(nums)
        output = [1] * n

        for i in range(1, n):
            output[i] = left
            left *= nums[i]


        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output
    
    def productExceptSelf(nums):
        n = len(nums)
        output = [1] * n

        # left pass
        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]

        # right pass
        right = 1
        for i in range(n-1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] * n 

        pref[0] = suff[n - 1] = 1

        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]

        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res

if __name__ == "__main__":
    sol = Solution()

    nums = [1,2,4,6]
    # nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]
    result = sol.productExceptSelf(nums)
    print(result)
        