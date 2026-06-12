class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m=len(nums)
        n=len(set(nums))
        if m==n:
            return False
        else:
            return True
