
#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        ret = 1
        back = 0
        for front in range(1, len(s)):
            for i in range(back, front):
                if s[i] == s[front]:
                    ret = max(front - back, ret)
                    back = i+1
                    break;
            if front == len(s)-1:
                ret = max(front + 1 - back, ret)
        return ret