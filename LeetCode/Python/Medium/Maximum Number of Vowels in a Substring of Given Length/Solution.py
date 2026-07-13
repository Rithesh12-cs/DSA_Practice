class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v="aeoiu"
        mx,n=0,len(s)
        cur=0
        for i in range(k):
            if s[i] in v:
                cur+=1
        mx=cur
        for i in range(k,n):
            if s[i] in v:
                cur+=1
            if s[i-k] in v:
                cur-=1
            mx=max(mx,cur)
        return mx