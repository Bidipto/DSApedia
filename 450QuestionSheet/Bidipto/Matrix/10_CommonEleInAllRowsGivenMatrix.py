from collections import Counter
# Common elements in all rows of a given matrix
mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]
#the will take a lot of modifications if duplicate elements are allowed
dic = Counter(mat[0])

for i in range(1,len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] in dic.keys() and dic[mat[i][j]] == i:
            dic[mat[i][j]] += 1
            if i == len(mat)-1:
                print(mat[i][j])
