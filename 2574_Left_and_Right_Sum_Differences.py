"""
Left and Right Sum Differences
Time Complexity: O(n²)
Space Complexity: O(n)
"""
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        LS=[]
        RS=[]
        num=nums[::-1]
        for i in range(len(nums)-1):
            c1=0
            c2=0
            for j in range(i+1,len(nums)):
                c1+=nums[j]
                c2+=num[j]
            RS.append(c1)
            LS.append(c2)
        RS.append(0)
        LS.append(0)
        final=LS[::-1]
        arr=[]
        for i in range(len(nums)):
            arr.append(abs(RS[i]-final[i]))
        return arr
        



