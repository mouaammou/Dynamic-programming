from typing import List

class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     # i dont want any solution yet, stop giving me suggestions

    #     row_len = len(matrix)
    #     col_len = len(matrix[0])
    #     l_row = 0
    #     r_row = row_len - 1
    #     while l_row <= r_row:

    #         mid_row = l_row + ((r_row - l_row) // 2)
    #         if matrix[mid_row][-1] < target:
    #             l_row = mid_row + 1
    #         elif matrix[mid_row][0] > target:
    #             r_row = mid_row - 1
    #         else:

    #             left = 0
    #             right = col_len - 1

    #             while left <= right:
    #                 if matrix[mid_row][0] == target:
    #                     return True
    #                 mid = left + ((right - left) // 2)
    #                 if matrix[mid_row][mid] == target:
    #                     return True
    #                 elif matrix[mid_row][mid] < target:
    #                     left = mid + 1
    #                 else:
    #                     right = mid - 1
                        
    #             return False

    #     return False



        def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            # i dont want any solution yet, stop giving me suggestions

            row_len = len(matrix)
            col_len = len(matrix[0])

            l = 0
            r = row_len * col_len - 1
            
            while l <= r:
                m = l + (r - l) // 2
                row = m // col_len
                col = m % col_len

                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] > target:
                    r = m - 1
                else:
                    l = m + 1
            
            return False












sol = Solution()
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3

print(sol.searchMatrix(matrix, target))  # Expected output: True