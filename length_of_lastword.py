"""
Length of Last Word
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        
        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # Count last word characters
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length
