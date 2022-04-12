# 921. Minimum Add to Make Parentheses Valid

def minAddToMakeValid(self, s: str) -> int:
    #count caounts the open parenthesis and then close them when when a close is found
    count = 0
    #count2 counts the parenthesis that are closedwithout an open parenthesis
    count2 = 0
    for i in list(s):
        if i == "(":
            count += 1
        else:
            if count > 0:
                count -= 1
            else:
                count2 += 1 
            
    return count + count2