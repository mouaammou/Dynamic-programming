from typing import List
from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {item: 0 for item in nums}
        for item in nums:
            hash_map[item] += 1
        # Sort by value in descending order
        # print(hash_map.items())
        sorted_items = sorted(hash_map.items(),key=lambda x: x[1], reverse=True)
        print(sorted_items)
        # print(hash_map.sort)
        res = []
        for i in range(k):
            res.append(sorted_items[i][0])
        # prrint(res)
        return res
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        for num in nums:
            my_map[num] = 1 + my_map.get(num, 0)

        heap = []

        for item in my_map:
            heapq.heappush(heap, (my_map[item], item))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            my_map[num] = 1 + my_map.get(num, 0)
        for num, cnt in my_map.items():
            freq[cnt].append(num)
        print(freq, len(freq), len(nums))

        return
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res    

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = {}
        for num in nums:
            my_map[num] = 1 + my_map.get(num, 0)
        
        counter = [[] for i in range(len(nums) + 1)]
        
        for num, cnt in my_map.items():
            counter[cnt].append(num)
        res = []
        for i in range(len(counter) - 1, 0, -1):
            for num in counter[i]:
                res.append(num)
                if k == len(res):
                    return res
        return res
            
if __name__ == "__main__":

    sol = Solution()
    nums=[1,1,1,2,2, 2,3, 3, 3, 3, 3, 3,3 ]
    k=2
    result = sol.topKFrequent(nums, k)
    print(result)