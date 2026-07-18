from math import gcd
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        l=max(nums)
        s=min(nums)
        return gcd(l,s)
