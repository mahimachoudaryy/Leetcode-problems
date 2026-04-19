"""
Reverse Integer(LeetCode)
Time Complexity: O(log n)
Space Complexity: O(1)
"""
class Solution:
    def reverse(self, x: int) -> int:
        negative=False
        if x<0:
            negative=True
            x=-x
        original=x
        reversed=0
        while x>0:
            digit=x%10
            reversed=reversed*10+digit
            x//=10
        if negative:
            reversed=-reversed
        if reversed<-2**31 or reversed>2**31-2:
            return 0
        return reversed
        