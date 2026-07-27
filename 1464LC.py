class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        a=len(nums)-1
        b=a-1
        return (nums[a]-1)*(nums[b]-1)
