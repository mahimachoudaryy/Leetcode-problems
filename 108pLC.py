class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        ar=[]

        for i in arr:
            if i==0:
                ar.append(i)
                ar.append(i)
            else:
                ar.append(i) 
        arr[:]=ar[:len(arr)]
