class Solution:
    def totalFruit(self, s: List[int]) -> int:
        freq={}
        l=0
        c,mc=0,0
        for r in range(len(s)):
            freq[s[r]]=freq.get(s[r],0)+1
            while len(freq) > 2:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    del freq[s[l]]
                l+=1
            mc=max(mc,r-l+1)
        return mc

        