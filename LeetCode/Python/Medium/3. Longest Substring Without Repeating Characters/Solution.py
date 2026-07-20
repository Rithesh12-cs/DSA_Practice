class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        maxlen=0
        l,n=0,len(s)
        for r in range(n):
            freq[s[r]]=freq.get(s[r],0)+1
            while(freq[s[r]] >1):
                freq[s[l]]-=1
                l+=1
            maxlen=max(maxlen,r-l+1)
        return maxlen