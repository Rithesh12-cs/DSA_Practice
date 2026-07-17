class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Apply Kadane's Algorithm
        cur,masum=nums[0],nums[0]
        for i in range(1,len(nums)):
            cur = max(nums[i],cur+nums[i])
            masum=max(masum,cur)
        return masum
        