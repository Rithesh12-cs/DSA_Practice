class Solution:
    def maxPower(self, s: str) -> int:
        c,mc=0,0
        for i in range(len(s)):
            if s[i]==s[i-1]:
                c+=1
                mc=max(mc,c)
            else:
                c=1
        return mc
        