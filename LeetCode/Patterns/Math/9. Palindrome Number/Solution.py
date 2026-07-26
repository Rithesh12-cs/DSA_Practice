class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        li=str(x)
        return li==li[::-1]