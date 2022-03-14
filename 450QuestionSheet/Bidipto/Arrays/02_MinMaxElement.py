# for loop with 2n number of comparasions
def getMinMax( a, n):
    minn = a[0]
    maxx = a[0]
    for i in a:
        if i>maxx:
            maxx = i
        elif i<minn:
            minn = i
    return minn, maxx

# a better solution with lesser number of comparasions is viable
# with uses elements in paires and compares them
def getMinMax( a, n):
    if n%2:
        minn = a[0]
        maxx = a[0]
        i = 1
    else:
        if a[0]>a[1]:
            minn = a[1]
            maxx = a[0]
        else:
            minn = a[0]
            maxx = a[1]
        i = 2
    while(i<n):
        if a[i]>a[i+1]:
            minn = min(minn, a[i+1])
            maxx = max(maxx, a[i])
        else:
            minn = min(minn, a[i])
            maxx = max(maxx, a[i+1])
        i += 2
    return minn, maxx