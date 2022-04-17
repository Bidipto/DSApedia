def gameOfLife(self, board: List[List[int]]) -> None:
    mat = [[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    # let 2 be 0 that has to be changed to 1
    # and 3 be 1 that has to be changed to 0
    M, N = len(board),len(board[0])
    for i in range(len(board)):
        for j in range(len(board[0])):
            count = 0
            #counting the number of 1s surrounding
            for m,n in mat:
                if 0<=i+m<M and 0<=j+n<N:
                    # print(i,j,i+m,j+n,board[i+m][j+n],count)
                    if board[i+m][j+n] == 1 or board[i+m][j+n] == 3:
                        count += 1
            # print(i,j,count)
            #for live cells:
            if board[i][j]:
                #less then 2 neighbours or more then 3 dies
                if count<2 or count>3:
                    board[i][j] = 3
            #for dead cells
            else:
                if count == 3:
                    board[i][j] = 2
    print(*board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 2:
                board[i][j] = 1
            elif board[i][j] == 3:
                board[i][j] = 0