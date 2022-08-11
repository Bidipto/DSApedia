# 875 · Longest Line of Consecutive One in Matrix

def longest_line(mat):
    M = len(mat)
    N = len(mat[0])
    res = 0
    for m in range(M):
        for n in range(N):
            if mat[m][n]:
                #down 
                c = 0
                i,j = m,n
                while mat[i][j]:
                    c += 1
                    i += 1
                    if i == M:
                        break 
                res = max(res,c)
                #right 
                c = 0
                i,j = m,n
                while mat[i][j]:
                    c += 1
                    j += 1
                    if j == N:
                        break 
                res = max(res,c)
                #diagonal
                c = 0
                i,j = m,n
                while mat[i][j]:
                    c += 1
                    i += 1
                    j += 1
                    if i == M or j == N:
                        break 
                res = max(res,c)
                #0diagonal
                c = 0
                i,j = m,n
                while mat[i][j]:
                    c += 1
                    i += 1
                    j -= 1
                    if i == M or j == -1:
                        break 
                res = max(res,c)
    return res
print(longest_line([[0,1,1,0,0],[0,1,1,0,0],[0,0,0,1,1],[1,0,0,1,0],[1,1,1,1,1]]))