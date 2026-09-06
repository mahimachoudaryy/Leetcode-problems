class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        t=1
        if num<=1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num%i==0:
                t+=i
                t+=num//i
        return t==num
