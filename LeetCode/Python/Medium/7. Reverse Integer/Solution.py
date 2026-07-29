class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign=-1
        else:
            sign=1
        temp=abs(x)
        rev=0
        while temp!=0:
            rem=temp%10
            rev=rev*10+rem
            temp//=10
        return sign*rev

        
        