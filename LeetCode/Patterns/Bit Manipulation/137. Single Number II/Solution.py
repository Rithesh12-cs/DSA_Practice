class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        res,n=0,len(nums)
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i in nums:
            cnt=freq.get(i,0)
            if cnt ==1:
                res=i
        return res

        