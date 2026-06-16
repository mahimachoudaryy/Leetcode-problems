class Solution:
    def processStr(self, s: str) -> str:
        ns=""
        for i in s:
            if i in "abcdefghijklmnopqrstuvwxyz":
                ns+=i
            if i == "#":
                ns=ns+ns
            if i == "*":
                ns=ns[:len(ns)-1]
            if i == "%":
                ns=ns[::-1]
        return ns
