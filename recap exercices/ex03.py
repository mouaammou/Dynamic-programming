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
    
    index = s1.index(s2[0])

    # print(s1[index:] + s1[:index])
    if (s1[index:] + s1[:index]) == s2:
        return True
    return False

if __name__ == '__main__':
    s1 = "abcde"

    s2 = "cdeab"

    s1 = "aab"
    s2 = "aba"

    result = isNonTrivialRotation(s1, s2)

    print((result))