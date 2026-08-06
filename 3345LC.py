class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        '''def answer(n,t):
                p=1
                for i in str(n):
                    p=p*int(i)
                if p%t==0:
                    return n
                return answer(n+1,t)
           return answer(n,t)'''
           #this is correct but lets see a more simpler one 
        while True:
            p = 1
            for d in str(n):
                p *= int(d)
            if p % t == 0:
                return n
            n += 1
        
