class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def genpar(n , oc ,cc,s):
            if (oc + cc ==  2 *n):
                res.append(s)
                return
            if (oc < n) :
                genpar( n , oc +1 ,cc, s+'(')
            if oc > cc:
                genpar( n , oc , cc +1 , s + ')')
            
        genpar( n , 0 , 0 ,"")
        return res
        