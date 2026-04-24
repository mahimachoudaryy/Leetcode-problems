"""
Longest Common Prefix
Find the longest common prefix string among an array of strings.
Time Complexity: O(n * m)
Space Complexity: O(1)
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix=strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix=prefix[:-1]
                if prefix=="":
                    return ""
        return prefix
