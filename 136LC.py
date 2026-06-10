class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    #   if(l==1):
     #       return nums[0]
    #  for i in range(0,):
     #       if(sorted(nums)[i]!=sorted(nums)[i+1]):
      #          return i
      return functools.reduce(lambda x,y: x^y, nums)
