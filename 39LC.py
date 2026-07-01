class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def generate(ind, curr, target):
            
            if target == 0:
                ans.append(curr.copy())
                return
            
            if target < 0 or ind == len(candidates):
                return
            curr.append(candidates[ind])
            generate(ind, curr, target - candidates[ind])
            curr.pop()
            generate(ind + 1, curr, target)
        ind=0
        ans = []
        generate(0, [], target)
        return ans
