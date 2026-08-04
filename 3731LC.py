class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mi=min(nums)
        mx=max(nums)
        ls=[]
        for i in range(mi,mx+1):
            if i not in nums:
                ls.append(i)
        return ls
