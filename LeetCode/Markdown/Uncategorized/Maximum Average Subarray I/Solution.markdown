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
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prefix=defaultdict(int)
        res,n=[],len(nums)
        cur=0
        #1.Element
        for i in range(k):
            prefix[nums[i]] +=1
            cur+=nums[i] #stores the current sum
        res.append(cur/k) #Add the 1 avg
        for i in range(k,n):
            prefix[nums[i]] +=1 #Adding the element at the first
            prefix[nums[i-k]]-=1 #Removing the element from the end

            if prefix[nums[i-k]]==0:
                del prefix[nums[i-k]] #To verify the element is removed or not
            cur+=nums[i] - nums[i-k] #To store the elemnt 
            res.append(cur/k)
        return max(res)
            
        
```