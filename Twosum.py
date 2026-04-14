"""
Two Sum Problem (Brute Force)
Return indices of two elements whose sum equals the given target.
Time Complexity: O(n^2)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return[i,j]