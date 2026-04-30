class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            left = 0
            right = 0

            if not s:
                return 0
            res = 0
            merged = set()

            for right in range(len(s)):
                while s[right] in merged:
                    merged.remove(s[left])
                    left += 1
                
                merged.add(s[right])
                res = max(res, right - left + 1)
            return res
            

s = "abaaaaaaaaaaaaaaaaaaaaaaaaaaaacb"
# s = "pwwkew"
# s = "xxxx"
print(Solution().lengthOfLongestSubstring(s))