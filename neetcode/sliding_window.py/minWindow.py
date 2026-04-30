class Solution:
    # def minWindow(self, s: str, t: str) -> str:

    #     freq = {}
    #     for c in t:
    #         freq[c] = 1 + freq.get(c, 0)

    #     min_len = float("inf")
    #     res = ""
    #     for i in range(len(s)):

    #         for j in range(i, len(s)):
    #             substr = s[i: j + 1]

    #             count_map = {}
    #             for c in substr:
    #                 count_map[c] = 1 + count_map.get(c, 1)

    #             valid = True
    #             for c in t:
    #                 if count_map.get(c, 0) < freq[c]:
    #                     valid = False
    #                     break
                
    #             if valid and len(substr) < min_len:
    #                 min_len = len(substr)
    #                 res = substr
    #     return res



    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for c in t:
            freq[c] = 1 + freq.get(c, 0)

        min_len = float("inf")
        res = ""

        left = 0
        checker_map = {}
        have = 0
        for right in range(len(s)):
            c = s[right]
            checker_map[c] = 1 + checker_map.get(c, 0)
            
            if c in freq and checker_map[c] == freq[c]:
                have += 1

            while len(freq) == have:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res = s[left: right + 1]
                
                checker_map[s[left]] -= 1

                if s[left] in freq and checker_map[s[left]] < freq[s[left]]:
                    have -= 1
                
                left += 1
   
        return res

        




            






s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))