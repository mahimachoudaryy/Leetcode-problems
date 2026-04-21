"""
Container With Most Water (Two Pointers)
Use two pointers to maximize area by moving the shorter line inward.
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0, len(height)-1
        ans=0
        while l<r:
            area=(r-l)*min(height[l],height[r])
            ans=max(ans,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans