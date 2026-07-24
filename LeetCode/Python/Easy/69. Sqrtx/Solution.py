class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return 0
        l,r=1,x//2
        while l<=r:
            mid=(l+r)//2
            res=mid*mid
            if res==x:
                return mid
            elif res < x:
                l=mid +1
            else:
                r=mid-1
        return r


        