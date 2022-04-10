#some intuition and logic
#give some time and think
def countRev (s):
    res = 0
    count = 0
    for i in s:
        if i == "{":
            count += 1
        else:
            if count:
                count -= 1
            else:
                res += 1
                count += 1
    if count % 2 == 0:
        return int(count/2) + res
    else:
        return -1