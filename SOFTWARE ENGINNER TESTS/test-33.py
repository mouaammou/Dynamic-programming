#
# Complete the 'allocateBandwidthMaxRevenue' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER_ARRAY sizes
#  3. INTEGER_ARRAY revenues
#  4. LONG_INTEGER B
#

def allocateBandwidthMaxRevenue(N, sizes, revenues, B):
    streams = []
    for i in range(N):
        streams.append((revenues[i] / sizes[i], sizes[i], revenues[i]))
    # print(streams)
    streams.sort(reverse=True)  # Sort by density descending

    total_revenue = 0.0
    for density, size, revenue in streams:
        if B >= size:
            total_revenue += revenue
            B -= size
        else:
            total_revenue += density * B
            break
    return total_revenue


if __name__ == '__main__':
    N = 3
    sizes = [10, 20, 30]
    revenues = [60, 100, 120]
    B = 50

    result = allocateBandwidthMaxRevenue(N, sizes, revenues, B)
    print(result)