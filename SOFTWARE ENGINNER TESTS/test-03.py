def isAlphabeticPalindrome(code):
    # Write your code here
    alpha_array = []
    for letter in code:
        if ord(letter) < 33 or ord(letter) > 126:
            return 0
        if 'a' <= letter <= 'z' or 'A' <= letter <= 'Z':
            alpha_array.append(letter.lower())
    # [start:stop:step] adds a step value, which tells Python how to move through the list.
    return int(alpha_array == alpha_array[::-1])
    

if __name__ == '__main__':

    print(isAlphabeticPalindrome(" "))

    