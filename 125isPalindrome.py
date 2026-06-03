class Solution:
    def isPalindrome(self, s: str) -> bool:
       # s=s.lower() #convert all the letters to small
      #  s=s.replace(" ","") #removes gaps
       # if(s==s[::-1]):
        #    return True
       # return False

        cleaned = ""
        for c in s:
            if c.isalnum():      # isalnum(is alphanumeric) keep letters and digits
                cleaned += c.lower()
        return cleaned == cleaned[::-1]

    # class Solution:
    #def isPalindrome(self, s: str) -> bool:
     #   left, right = 0, len(s) - 1

     #   while left < right:
            # move left until alphanumeric
     #       while left < right and not s[left].isalnum():
    #            left += 1
            
            # move right until alphanumeric
      #      while left < right and not s[right].isalnum():
     #           right -= 1
            
            # compare lowercase characters
     #       if s[left].lower() != s[right].lower():
      #          return False

      #      left += 1
       #     right -= 1

      #  return True. (another method of solving the quetion)
