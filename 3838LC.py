class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alf="abcdefghijklmnopqrstuvwxyz"
        arr=[]
        for w in words:
            c=0
            for l in w:
                for i in range(26):
                    if alf[i]==l:
                        c+=weights[i]
            arr.append(c%26)
        r=alf[::-1]
        ns=""
        for j in arr:
            ns+=r[j]
        return ns
