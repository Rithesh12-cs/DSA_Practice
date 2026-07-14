class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #Spliting based on k
        n=len(cardPoints)
        sc=sum(cardPoints[:k])
        ma=sc
        for i in range(1,k+1):
            sc-=cardPoints[k-i]
            sc+=cardPoints[n-i]
            ma=max(sc,ma)
        return ma
        