class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt,res={},0
        for i in word:
            cnt[i]=cnt.get(i,0)+1
        freq=sorted(cnt.values(),reverse=True)
        for i,fre in enumerate(freq):
            pn=(i//8)+1
            res+=fre*pn
        return res