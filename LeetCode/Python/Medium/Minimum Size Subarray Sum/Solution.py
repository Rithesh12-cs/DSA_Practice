class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l= 0
        s, n = 0, len(nums)
        l, res = 0, float("inf")
        for r in range(n):
            s += nums[r]
            while s >= target:
                res = min(res, r - l + 1)
                s -= nums[l]
                l += 1
        return res if res!=float('inf') else 0

            

        