# 241. Different Ways to Add Parentheses

#we cant hash lists lel 
def diffWaysToCompute(self, num: str) -> List[int]:
        stack = []
        val = 0
        for i in num:
            if i.isdigit():
                val *= 10
                val += int(i)
            else:
                stack.append(val)
                stack.append(i)
                val = 0
        stack.append(val)
        
        @cache
        def magic(stack):
            # print(stack)
            if len(stack) == 1:
                return stack
            
            res = []
            for i in range(1,len(stack),2):
                left = magic(stack[:i])
                right = magic(stack[i+1:])
                sign = stack[i]
                # print(left,sign,right)
                
                if sign == "+":
                    for a,b in product(left,right):
                        # print(sign,a,b)
                        res.append(a+b)
                elif sign =="-":
                    for a,b in product(left,right):
                        # print(sign,a,b)
                        res.append(a-b)
                else:
                    for a,b in product(left,right):
                        res.append(a*b)
            return res
            
       
        
        
        return magic(tuple(stack))