class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        sa=[]
        la=[]
        p=[]
        for i in nums:
            if i==pivot:
                p.append(i)
            elif(i<pivot):
                sa.append(i)
            else:
                la.append(i)
        return sa+p+la
