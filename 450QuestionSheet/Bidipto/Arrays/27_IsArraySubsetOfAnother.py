#is there a better approach
def isSubset( a1, a2, n, m):
    a1 = set(a1)
    a2 = set(a2)
    for i in a2:
        if i not in a1:
            return "No"
    return "Yes"