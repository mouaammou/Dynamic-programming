class Solution:
    def isPalindrome(self, s: str) -> bool:
        
       
        left = 0
        right = len(s) - 1

        while left <= right:

            while s[left].isalnum() is False:
                left += 1
            while s[right].isalnum() is False:
                right -= 1

            left_char = s[left].lower()
            right_char = s[right].lower()

            if left_char != " " and right_char != " " and left_char.isalnum() and right_char.isalnum():

                if left_char != right_char:
                    return False
            
            left += 1
            right -=1

        return True

if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    # s = "tab a cat"
    s = "0P"
    sol = Solution()
    # Call the solution here when ready
    print(sol.isPalindrome(s))