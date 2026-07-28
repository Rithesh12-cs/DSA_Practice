class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        rs,ls="",""
        m=n//2
        ll = sorted(s[:m])
        rr=list(reversed(ll))
        mid=[s[m]] if n%2!=0 else []
        return "".join(ll+mid +rr)
        