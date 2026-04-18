"""
Longest Palindromic Substring (Brute Force)
Check all substrings and return the longest palindrome.
Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        arr=[]
        for i in range(len(s)):
            for j in range(i,len(s)):
                ans=s[i:j+1]
                if(ans==ans[::-1]):
                    arr.append(ans)
        final=""
        for i in arr:
            if len(i)>len(final):
                final=i
        return final