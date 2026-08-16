class Solution:
    def toLowerCase(self, s: str) -> str:
        ans=""
        for ch in s:
            if 'A'<=ch<='Z':
                ch=chr(ord(ch)+32)
            ans+=ch
        return ans
