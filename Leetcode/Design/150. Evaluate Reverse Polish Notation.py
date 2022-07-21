# 150. Evaluate Reverse Polish Notation

def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        check = {"+","-","*","/"}
        for i in tokens:
            # print(i,stack)
            if i in check:
                a= stack.pop()
                b = stack.pop()
                if i == "+":
                    temp = b + a
                elif i == "-":
                    temp = b - a
                elif i == "*":
                    temp = b * a
                else:
                    temp = int(b/a)
                    # print(b,a,temp)
                stack.append(temp)
            else:
                stack.append(int(i))
                 
        return stack[0]