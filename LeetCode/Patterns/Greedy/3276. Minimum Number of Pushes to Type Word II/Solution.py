class Solution:
    def minimumPushes(self, word: str) -> int:
        freq={}
        res=0
        for i in word:
            freq[i]=freq.get(i,0)+1
        
        freq_sort=sorted(freq.values(),reverse=True)
        i=0
        for cnt in freq_sort:
            push=(i//8)+1
            res +=push*cnt
            i+=1
        return res
        