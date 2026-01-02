#
# Complete the 'isNonTrivialRotation' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

# def isNonTrivialRotation(s1, s2):
#    if any(char.isupper() for char in s1) or any(char.isupper() for char in s2) or len(s1) != len(s2):
#       return False
#    first_index = -1
#    if s2[0] in s1:
#       first_index = s1.index(s2[0])
#       if first_index == -1:
#          return False
   
#    new_str = s1[:first_index] + s2[first_index:]
#    print("0 -- index: ", s1[:first_index])
#    print("index -- fin: ",s1[first_index:])
#    print(new_str)
#    if s1 != s2 and new_str == s1:
#       return True
#    return False

def isNonTrivialRotation(s1, s2):
    if any(char.isupper() for char in s1) or any(char.isupper() for char in s2) or len(s1) != len(s2):
        return False
    if s1 == s2:
        return False  # Non-trivial means not the same
    return s2 in (s1 + s1)


if __name__ == '__main__':
   s1 = "xyz123xyz123"
   s2 = "3xyz12"
   print(isNonTrivialRotation(s1, s2))  # Should be True, but returns FalseTrue, but returns False