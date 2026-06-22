class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val=[]
        for i in tokens:
            if i=="+" or i=="-" or i=="*" or i=="/":
                if not val:
                    return 
                else:
                    a=val.pop()
                    b=val.pop()
                    if i=="+":
                        val.append(b+a)
                    elif i=="-":
                        val.append(b-a)
                    elif i=="*":
                        val.append(b*a)
                    elif i=="/":
                        val.append(int(b/a))
            else:
                val.append(int(i))
        return int(val[0])
