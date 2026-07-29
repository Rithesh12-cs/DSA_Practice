class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN,INT_MAX=-2**31,2**31 -1
        if x < 0:
            sign=-1
        else:
            sign=1
        temp=abs(x)
        rev=0
        while temp!=0:
            rem=temp%10
            if rev > (INT_MAX - rem) //10:
                return 0
            rev=rev*10+rem
            temp//=10
        return sign*rev

        
        