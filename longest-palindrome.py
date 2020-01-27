class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""
        ret = s[0]
        for i in range(0, len(s)):
            add = 1
            while i - add >= 0 and i + add < len(s) and s[i - add] == s[i + add]:
                if 1 + (2 * add) > len(ret):
                    ret = s[i - add:i + add + 1]
                add += 1

            if i + 1 == len(s) or s[i] != s[i+1]:
                continue
            add = 0
            while i - add >= 0 and i + add + 1 < len(s) and s[i - add] == s[i + add + 1]:
                if 2 * (add+1) > len(ret):
                    ret = s[i - add:i + add + 2]
                add += 1
        return ret