class Solution:
    def findErrorNums(self,nums: List[int]) -> List[int]:
        s=set()
        dup,n=-1,len(nums)
        for i in nums:
            if i in s:
                dup=i
            s.add(i)
        total,miss=0,0
        total=(n*(n+1))//2
        miss=sum(nums)
        res=total-(miss-dup)
        return [dup,res]
        