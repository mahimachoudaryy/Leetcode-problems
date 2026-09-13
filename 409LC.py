class Solution:

    def longestPalindrome(self, s: str) -> int:

        d = {}

        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        c = 0
        odd = False

        for i, j in d.items():
            if j % 2 == 0:
                c += j
            else:
                c += j - 1
                odd = True

        if odd:
            c += 1

        return c
        # the odd part of code was suggested by gpt bcz, So whenever you have at least one odd count, you can add 1 at the end.
