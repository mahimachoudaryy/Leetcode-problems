from itertools import permutations
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        nums=set(permutations(digits,3))
        count=0
        for i in nums:
            if i[0]!=0 and i[2]%2==0:
                count+=1
        return count
