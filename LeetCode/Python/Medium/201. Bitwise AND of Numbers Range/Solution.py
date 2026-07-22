class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res=left
        for i in range(left,right):
            res&=i+1
            if res==0:
                return 0
        return res
        