class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr=[]
        for i in nums:
            s=str(i)
            c=0
            for j in s:
                c+=int(j)
            arr.append(c)
        return min(arr)
