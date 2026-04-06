
def maxDistinctSubstringLengthInSessions(sessionString):
    
    def sliding_window(sessionString):

        first_window = set()
        for char in sessionString:
            if char in first_window:
                break
            first_window.add(char)

        k = len(first_window)
        start = 0
        end = k - 1
        max_len = k
        while end < len(sessionString) - 1:
            end += 1
            if sessionString[end] not in first_window:
                first_window.add(sessionString[end])
            if sessionString[start] in first_window:
                first_window.remove(sessionString[start])
            start += 1
            max_len = max(max_len, len(first_window))

        return max_len
    
    all_strings = sessionString.split("*")
    array = []
    for string in all_strings:
        array.append(sliding_window(string))
    return max(array)


def maxDistinctSubstringLengthInSessions(sessionString):

    def max_distinct_window(s):
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # Shrink window from left until no duplicate
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

    return max(max_distinct_window(s) for s in sessionString.split("*"))


if __name__ == '__main__':
    sessionString = "abcdefabcabcdefgbb\"abcdefabcabcdefghbb"

    result = maxDistinctSubstringLengthInSessions(sessionString)

    print(result)