def isAnagram(s, t):
    # Write your code here
    if len(s) != len(t):
        return 0
    hash1 = {}
    hash2 = {}
    for value in s:
        if value in hash1:
            hash1[value] += 1
        else:
            hash1[value] = 1

    for value in t:
        if value in hash2:
            hash2[value] += 1
        else:
            hash2[value] = 1

    for i in range(len(s)):
        # print('hash1: ', hash1[s[i]] )
        # print('hash2: ', hash1[t[i]] )
        if hash1[s[i]] != hash2[s[i]]:
            return 0

    return 1

if __name__ == '__main__':
    s = "listen"
    t = "silent"

    result = isAnagram(s, t)

    print(result)