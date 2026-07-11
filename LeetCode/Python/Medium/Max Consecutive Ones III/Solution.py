class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        freq={}
        c,mc=0,0
        l=0
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1

            while freq.get(0,0) > k:
                freq[nums[l]]-=1
                if freq[nums[l]]==0:
                    del freq[nums[l]]
                l+=1
            mc=max(mc,i-l+1)
        return mc
        