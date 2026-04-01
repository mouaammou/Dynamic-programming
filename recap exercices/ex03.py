#
# Complete the 'isNonTrivialRotation' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def isNonTrivialRotation(s1, s2):
    # Write your code here
    if s1 == s2 or len(s1) != len(s2):
        return False
    

    # print(s1[index:] + s1[:index])
    # for i in range(len(s1)):
    #     if (s1[i:] + s1[:i]) == s2:
    #         return True
    if s2 in (s1+s1):
        return True
    return False

if __name__ == '__main__':
    s1 = "abcde"

    s2 = "cdeab"

    s1 = "abcd"
    s2 = "cdab"


    result = isNonTrivialRotation(s1, s2)

    print((result))