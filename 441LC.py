class Solution:
    def arrangeCoins(self, n: int) -> int:
        r=1
        c=0
        while n>=r:
            n-=r
            c+=1
            r+=1
        return c
