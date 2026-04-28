"""
Combination Sum II (Backtracking)
Time Complexity: O(2^n)
Space Complexity: O(n)
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
         def gener(ind,ans,curr,candidates,target):
            if(target==0):
                ans.append(curr.copy())
                return
            if(target<0):
                return
            if(ind==len(candidates)):
                return
            curr.append(candidates[ind])
            gener(ind+1,ans,curr,candidates,target-candidates[ind])
            curr.pop()
            for i in range (ind+1,len(candidates)):
                if (candidates[ind]!=candidates[i]):
                    ind = i
                    gener(ind,ans,curr,candidates,target) 
                    break
         ind=0
         ans=[]
         curr=[]
         candidates.sort()
         gener(ind,ans,curr,candidates,target)
         return ans
            
