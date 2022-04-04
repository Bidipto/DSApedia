#just interating the literal the given number of times
def countAndSay(self, n: int) -> str:
    lst = [1]
    for i in range(1,n):
        templst = []
        temp = lst[0]
        count = 0
        for i in lst:
            if temp == i:
                count += 1
            else:
                templst.append(count)
                templst.append(temp)
                temp = i
                count = 1
        templst.append(count)
        templst.append(temp)
        lst = templst
    return "".join([str(i) for i in lst])