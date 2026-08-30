class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0] * (n + 1)

        for i in range(1, n + 1):
            arr[i] = arr[i >> 1] + (i & 1)

        return arr



                #arr=[]
                #for i in range(n+1):
                #    a=bin(i)[2:]
                #    c=0
                #    for j in a:
                #        if j=="1":
                #            c+=1
                #    arr.append(c)
                #return arr. code correct eh but he did not allow using Bin as it is a built in function 
