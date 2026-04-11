#
# Complete the 'findZeroSumTripletsInWindow' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY readings
#  2. INTEGER windowSize
#

def findZeroSumTripletsInWindow(readings, windowSize):
    n = len(readings)
    result = set()  # use set to avoid duplicates efficiently

    for start in range(n):
        end = min(start + windowSize, n)

        # extract and sort current window
        window = readings[start:end]
        window.sort()

        # 3Sum using 2 pointers
        for i in range(len(window) - 2):
            # skip duplicates
            if i > 0 and window[i] == window[i - 1]:
                continue

            left = i + 1
            right = len(window) - 1

            while left < right:
                s = window[i] + window[left] + window[right]

                if s == 0:
                    result.add((window[i], window[left], window[right]))

                    left += 1
                    right -= 1

                    # skip duplicates
                    while left < right and window[left] == window[left - 1]:
                        left += 1
                    while left < right and window[right] == window[right + 1]:
                        right -= 1

                elif s < 0:
                    left += 1
                else:
                    right -= 1

    return [list(t) for t in result]

if __name__ == '__main__':

    readings = [1, -2, 1, 0, 5]
    windowSize = 3

    result = findZeroSumTripletsInWindow(readings, windowSize)

    print('\n'.join([' '.join(map(str, x)) for x in result]))