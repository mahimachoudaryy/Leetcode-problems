"""
Find the Index of the First Occurrence in a String
Time Complexity: O(n * m)
Space Complexity: O(1)
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        n=len(haystack)
        m=len(needle)
        for i in range(n-m+1):
            if haystack[i:i+m]==needle:
                return i
        return -1
