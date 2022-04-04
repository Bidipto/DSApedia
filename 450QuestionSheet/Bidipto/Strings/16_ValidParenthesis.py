def isValid(self, s):
    stack=[]
    dic={"(":")","[":"]","{":"}"}
    for i in s:
        if i in dic:
            stack.append(dic[i])
        elif not stack or stack.pop()!=i:
            return False
    return not stack