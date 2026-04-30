class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) + 1

        window = len(s1)
        window_map = {}

        for c in s2[:window]:
            window_map[c] = window_map.get(c, 0) + 1

        if window_map == freq:
            return True


        left = 0
        for right in range(window, len(s2)):
            window_map[s2[right]] = window_map.get(s2[right], 0) + 1

            window_map[s2[left]] -= 1
            if window_map[s2[left]] == 0:
                del window_map[s2[left]]

            left += 1

            if window_map == freq:
                return True

        return False

s1 = "abc"
s2 = "lecabee"
# s1 = "ab"
# s2 = "dd"
# # s1 = "aab"
# # s2 = "baa"
print(Solution().checkInclusion(s1, s2))