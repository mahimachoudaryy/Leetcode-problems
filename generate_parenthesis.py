"""
Generate Parentheses (Backtracking)
Time Complexity: O(2^n)
Space Complexity: O(n)
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(curr,open,close,ans,n):
            if (open + close==2*n and open ==close):
                ans.append(curr)
                return
            if (open >n):
                return 
            if (close>open):
                return
            generate (curr+"(",open+1,close,ans,n)
            generate (curr+")",open,close+1,ans,n)
        ans=[]
        curr=""
        open=0
        close=0
        generate(curr,open,close,ans,n)
        return ans
