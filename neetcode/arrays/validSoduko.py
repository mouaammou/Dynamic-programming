from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        len_r = len(board)
        len_c = len(board[0])
        # to check the rows one by one
        for i in range(len_r):
            seen = set()
            for j in range(len_c):
                if board[i][j] == '.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        # to check the columns one by one
        for i in range(len_r):
            seen = set()
            for j in range(len_c):
                if board[j][i] == '.':
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])
               

        # check 3*3 range everytime
        for square in range(len_r):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j

                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
                



if __name__ == "__main__":
    sol = Solution()
    board = [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]
    
    result = sol.isValidSudoku(board)
    print(result)