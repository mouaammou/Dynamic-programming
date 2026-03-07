#
# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
#



def isAlphabeticPalindrome(code):
    # Write your code here
    new_str = []

    for c in code:
        if c.isalpha():
            new_str.append(c.lower())
    
    # print("newstr: ", new_str)
    len_str = len(new_str) // 2

    for i in range(len_str):
        # print("i", new_str[i])
        # print("j", new_str[len(new_str) - 1 - i])

        if new_str[i] != new_str[len(new_str) - 1 - i]:
            return 0
    return 1

# CLAUDE SOLUTION : For typical interview/competitive contexts, the slice version is cleaner to write quickly    

def isAlphabeticPalindrome(code):
    filtered = [c.lower() for c in code if c.isalpha()]
    print("filterd str: ", filtered[::-1])
    return 1 if filtered == filtered[::-1] else 0

if __name__ == '__main__':
    code = "mouad"

    result = isAlphabeticPalindrome(code)

    print(result)
