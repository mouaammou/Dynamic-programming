


def count_max_3_elements(array):
    k = 3
    start = 0
    end = k - 1
    window_sum = sum(array[start:end+1])
    max_win = window_sum
    while end < len(array) - 1:
        end += 1
        window_sum += array[end] - array[start]
        max_win = max(max_win, window_sum)
        start += 1
    return max_win


if __name__ == '__main__':
    array = [2, 1, 5, 1, 3, 2, 8]
    result = count_max_3_elements(array)
    print(result)