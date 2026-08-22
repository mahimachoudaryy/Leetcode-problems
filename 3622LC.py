class Solution:
    def checkDivisibility(self, n: int) -> bool:
        org=n
        sum=0
        product=1
        while n>0:
            digits=n%10
            sum+=digits
            product*=digits
            n//=10
        return org%(sum+product)==0
