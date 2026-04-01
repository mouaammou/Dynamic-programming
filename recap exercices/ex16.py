def minTasksToCancelForNoConflict(digits):
    if not digits:
        return []

    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        '0': '0', '1': '1'
    }

    result = []

    def backtrack(index, current):
        if index == len(digits):        # base case: used all digits
            result.append(current)
            return
        for letter in phone_map[digits[index]]:  # try each letter
            backtrack(index + 1, current + letter)

    backtrack(0, "")
    return result



if __name__ == '__main__':
    digits = input()

    result = minTasksToCancelForNoConflict(digits)

    print('\n'.join(result))