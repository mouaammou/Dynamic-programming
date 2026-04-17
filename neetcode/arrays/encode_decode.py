from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = "".join(f"{len(s)}#{s}" for s in strs)
        
        return encoded_str

        

    def decode(self, s: str) -> List[str]:
        
        i = 0
        j = 0
        res = []
        while (i < len(s)):

            j = i
            while (s[j] != '#'):
                j+= 1
            
            len_s = int(s[i:j])
            res.append(s[j+1: j + 1 + len_s])

            i = j + 1 + len_s
        
        return res


if __name__ == "__main__":

    sol = Solution()
    strs = ["we","sdsd"]
    # strs =[""]

    result = sol.encode(strs)
    result = sol.decode(result)

    print(result)