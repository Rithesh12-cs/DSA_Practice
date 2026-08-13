import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Optimal(BS)
        #piles.sort()
        low, high = 1, max(piles) +1
        ans = max(piles)
        while low <= high:
            res = 0
            mid = (low + high)// 2
            for pile in piles:
                res += math.ceil(pile / mid)
            if res <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
