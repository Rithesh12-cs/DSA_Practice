class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        lis=set()
        def generate(idx , cur):
            if len(cur) >= 2:
                lis.add(tuple(cur))
            for i in range(idx , len(nums)):
                if not cur or nums[i] >= cur[-1]:
                    generate(i+1,cur + [nums[i]])
        generate(0, [])
        x=list(lis)
        return x



