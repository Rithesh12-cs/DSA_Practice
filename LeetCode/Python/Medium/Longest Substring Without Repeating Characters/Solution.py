class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        c,mc=len(s),0
        l=0
        for i in range(c):
            ch=set()
            for j in range(i,c):
                char=s[j]
                if char in ch:
                    break
                ch.add(char)
                mc=max(mc,j-i+1)
        return mc
        