# 282. Expression Add Operators

def addOperators(self, num: str, target: int) -> List[str]:
    N = len(num)
    res = []
    
    def magic(i, summ, stack, curr):
        # print(i, summ, stack, curr)
        if i == N:
            if summ == target:
                res.append(curr)
            return 
        #check for leading zeros
        if num[i] == "0":
            end = i + 1
        else:
            end = N
            
        val = 0
        s = ""
        if i == 0:
            for i in range(i,end):
                val *= 10
                val += int(num[i])
                s += num[i]
                #addition
                magic(i+1, summ + val, stack + [val],s)

        else:
            last = stack[-1]
            last = stack.pop()
            
            for i in range(i,end):
                val *= 10
                val += int(num[i])
                s += num[i]
                #addition
                magic(i+1, summ + val, stack + [last,val],curr + '+' + s)
                #substract
                magic(i+1, summ - val, stack + [last,-val],curr + '-' + s)

                product = last*val
                #product
                magic(i+1, summ - last + product, stack + [product],curr + '*' + s)
                #div
                #lol when beyond the question
                # if val != 0:
                #     div = int(last/val)
                #     magic(i+1, summ - last + div, stack + [div],curr + '/' + s)


        
        
        magic(0,0,[],"")
        return res