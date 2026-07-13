# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        cur = 0
        res, n = 0, len(nums)
        for i in range(k):
            freq[nums[i]] += 1
            cur += nums[i]
            if len(freq) == k:
                res = cur
        for i in range(k, n):
            freq[nums[i]] += 1
            cur += nums[i]
            freq[nums[i - k]] -= 1
            cur -= nums[i - k]
            if freq[nums[i - k]] == 0:
                del freq[nums[i - k]]

            if len(freq) == k:
                res = max(res, cur)
        return res

```