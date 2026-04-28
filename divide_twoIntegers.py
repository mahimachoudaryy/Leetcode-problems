"""
Divide Two Integers
Time Complexity: O(1)
Space Complexity: O(1)
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        i=int(dividend/divisor)
        return i
