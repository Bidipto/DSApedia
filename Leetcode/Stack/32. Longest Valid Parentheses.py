# 32. Longest Valid Parentheses

def longestValidParentheses(self, s: str) -> int:
        #-1 in the stack means 0 se sab sorted ha
        #if we find a ( in 0th position stack will be [-1,0]
        #where as if we find a ) in 0th stack will be [0]
        #ie 0 ke badd se sab sorted ha 
        #the first element is like the mark after which all the elements are sorted 
        #instead of the first element we can maintain another variable too
        stack = [-1]
        res = 0
        
        for i,val in enumerate(s):
            if val == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack: 
                    res = max(res,(i-stack[-1]))
                else:
                    stack.append(i)
        
        return res