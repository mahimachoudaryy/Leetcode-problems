"""
3Sum Closest (Sorting + Two Pointers)
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans= nums[0] + nums[1] + nums[2] # sum of starting 3
        for i in range(len(nums)):
            low= i + 1
            high= len(nums) - 1 
            while low<high: # until indx is out of bound
                s = nums[i] + nums[low] + nums[high] 
                if abs(s - target) < abs(ans- target):
                    ans = s  # checking if the element chose now is closer or the before ome is 
                if s < target:
                    low=low+1 # moving or checking only left
                elif s > target:
                    high=high-1 # moving or checking only to right 
                else:
                    return s   # exact match
        return ans
