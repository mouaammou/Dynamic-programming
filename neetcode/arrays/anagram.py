class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count1 = {i: 0 for i in s}
        count2 = {i: 0 for i in t}

        for i in range(len(s)):
            count1[s[i]] += 1

        for i in range(len(t)):
            count2[t[i]] += 1

        return count1 == count2
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for c in t:
            count[ord(c) - ord('a')] -= 1
        
        print(count)
        for t in count:
            if t != 0:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    s="racecar"
    t="carrace"


    result = sol.isAnagram(s, t)
    print(result)
