"""
Longest Substring Without Repeating Characters
Find the length of the longest substring with all unique characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0
        maxl=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            maxl=max(maxl,right-left+1)
        return maxl
             