class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1,freq2={},{}
        n,m=len(s1),len(s2)
        for r in range(n):
            freq1[s1[r]]=freq1.get(s1[r],0)+1
        l=0
        for r in range(m):
            freq2[s2[r]]=freq2.get(s2[r],0) +1
            if r-l+1 > n:
                freq2[s2[l]]-=1
                if freq2[s2[l]]==0:
                    del freq2[s2[l]]
                l+=1
            if freq1==freq2:
                return True
        return False

        