class Solution:
    def smallestPalindrome(self, s: str) -> str:
        d={}
        if len(s)==1:
            return s
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        dic=sorted(d)
        S=""
        middle=""
        for j in dic:
            if d[j]!=1:
                for k in range(d[j]//2):
                    S+=j
            if d[j]%2 == 1:
                middle+=j
        return S+middle+S[::-1]
