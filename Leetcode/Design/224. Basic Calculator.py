# 224. Basic Calculator
# stack implementation 
def calculate(self, s: str) -> int:
        def update(sign, element):
            if sign == "+":
                stack.append(element)
            elif sign == "-":
                stack.append(-element)
                    
        i = 0
        num = 0
        stack = []
        sign = "+"
        N = len(s)

        while i<N:
            if "0"<=s[i]<="9":
                num *= 10
                num += int(s[i])
            elif s[i] in "+-":
                update(sign,num)
                num = 0
                sign = s[i]
            elif s[i] == "(":
                num, j = self.calculate(s[i+1:])
                i += j
            elif s[i] == ")":
                update(sign, num)
                return sum(stack), i + 1
            i += 1

        update(sign, num)
        return sum(stack)
