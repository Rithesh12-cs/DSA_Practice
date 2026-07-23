class Solution:
    def reverseBits(self, n: int) -> int:
        b=bin(n).replace('0b',"")
        res=b.zfill(32)
        n=list(res)
        n=n[::-1]
        re="".join(n)
        ans=int(re,2)
        return ans
        