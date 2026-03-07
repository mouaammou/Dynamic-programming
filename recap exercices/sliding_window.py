



def maxSumFixed(arr, k):
    # Build first window
    window_sum = sum(arr[:k]) # 
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]       # add incoming element
        window_sum -= arr[i - k]   # remove outgoing element
        max_sum = max(max_sum, window_sum)

    return max_sum

maxSumFixed([2, 1, 5, 1, 3, 2], k=3) # 9  (subarray [5,1,3])

# Here’s the O(n²) solution that recalculates the sum for every subarray of size

# def maxSumFixed_brute(arr, k):
#     max_sum = float('-inf')
#     for i in range(len(arr) - k + 1):
#         current_sum = sum(arr[i:i+k])
#         max_sum = max(max_sum, current_sum)
#     return max_sum

# Example usage:
import time

arr = [1] * 10000  # Large array
k = 5000           # Large window size

start = time.time()
result = maxSumFixed(arr, k)
end = time.time()

print(f"Result: {result}, Time taken: {end - start:.2f} seconds")