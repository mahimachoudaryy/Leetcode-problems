class Solution:
    def maxProduct(self, n: int) -> int:
        arr=[]
        for i in str(n):
            arr.append(int(i))
        ma=0
        for j in range(0,len(arr)-1):
            for k in range(j+1,len(arr)):
                nma=arr[j]*arr[k]
                ma=max(ma,nma)
        return ma
