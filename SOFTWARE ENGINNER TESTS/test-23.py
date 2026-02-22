
#
# Complete the 'verifySameMultisetDifferentStructure' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER_ARRAY root1
#  2. INTEGER_ARRAY root2
#




# def verifySameMultisetDifferentStructure(root1, root2):
#     # Write your code here
#     """
#         brute force:
#         1 - remove nulls
#         2 - remove duplicates
#         3 - sort
#         4 - compare them
#     """
#     if root1 == root2:
#         return False
#     while 100001 in root1:
#         root1.remove(100001)
#     while 100001 in root2:
#         root2.remove(100001)
    
#     # root1 = list(dict.fromkeys(root1))


#     # root2 = list(dict.fromkeys(root2))

#     # root1.sort()
#     # root2.sort()

#     # if root1 == root2:
#     #     return True
#     # return False

#     a = root1[0]
#     b = root2[0]
#     print(root1,root2,a,b)
#     for _, item in enumerate(root1, 1):
#         a += item
#         # print(item, index)

#     for _, item in enumerate(root2, 1):
#         b += item
#     print(a, b)
#     if a == b:
#         return True
#     return False
    
# def verifySameMultisetDifferentStructure(arr1, arr2):
#     # if len(arr1) != len(arr2):
#     #     return False

#     freq1 = {}
#     freq2 = {}
#     isRemove = False
#     while 100001 in arr1:
#         arr1.remove(100001)
#     while 100001 in arr2:
#         arr2.remove(100001)
#     # print(arr1, arr2)
#     if arr1 == arr2:
#         return False
#     # Count frequencies for arr1
#     for num in arr1:
#         # if num != 100001: 
#         freq1[num] = freq1.get(num, 0) + 1

#     # Count frequencies for arr2
#     for num in arr2:
#         # if num != 100001: 
#         freq2[num] = freq2.get(num, 0) + 1
#     # print(freq1,freq2)
#     return freq1 == freq2


def verifySameMultisetDifferentStructure(root1,root2):

    null_value = 100001

    values1 = [i for i in root1 if i != null_value]
    values2 = [j for j in root1 if j != null_value]

    if sorted(values1) != sorted(values2):
        return False

    strut1 = [1 if x != null_value else 0 for x in root1]
    strut2 = [1 if x != null_value else 0 for x in root2]

    if strut1 == strut2:
        return False
    return True


if __name__ == '__main__':

    root1 = [4, 2, 5, 1, 3, 100001, 100001]
    root2 = [3, 1, 5, 100001, 2, 4, 100001]

   

    result =  verifySameMultisetDifferentStructure(root1,root2)#verifySameMultisetDifferentStructure(root1, root2)

    print((result))

    # root1 = (dict.fromkeys(root1))
    # root2 = (dict.fromkeys(root2))
    # print(root1)
    # print(root2)
    # array = list({5: None, 3: None, 2: None, 2: None, 2: None, 2: None})
    # print(array)