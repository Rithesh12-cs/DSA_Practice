class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l,r=1,x//2
        while l<=r:
            mid=(l+r)//2
            res=mid*mid
            if res==x:
                return mid
            elif res < x:
                l+=1
            else:
                r-=1
        return r


        