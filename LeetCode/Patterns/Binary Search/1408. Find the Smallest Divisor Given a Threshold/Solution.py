import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        #1.Brute Force
        '''for i in range(1, max(nums)+1):
            res=0
            for j in range(len(nums)):
                res += math.ceil(nums[j] / i)

            if res <= threshold :
                return i
        return 1 '''
        #2.Binary Search
        low,high=1,max(nums)
        ans=high
        while low <= high :
            mid = (low+high)//2
            res = 0
            for i in nums:
                res += math.ceil(i/mid)
            if res <= threshold : 
                ans = mid
                high = mid -1 
            else:
                low = mid +1
        return ans

        