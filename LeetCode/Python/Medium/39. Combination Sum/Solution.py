class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        def pick(idx , target, li,res):
            #Base Condition :1
            if target ==  0:
                res.append(li)
                return
            #Base Conditon :2 
            if idx >= len(candidates)  or target < 0:
                return 
            #To pick the element
            pick(idx ,target-candidates[idx],li + [candidates[idx]],res)
            #To not to pick the element
            pick(idx +1 , target , li , res)
        
        pick(0,target,[],res)
        return res