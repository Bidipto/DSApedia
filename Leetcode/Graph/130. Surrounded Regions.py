# 130. Surrounded Regions
# dfs with twists, modified the way to solve to cater to the uniquiness of the question
def solve(self, board: List[List[str]]) -> None:
        def magic(i,j):
            if board[i][j] == 'X':
                return 
            else:
                board[i][j] = -1
                
            for m,n in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=m<M and 0<=n<N and board[m][n] == 'O':
                    magic(m,n)
                    
            return 
        
        M = len(board)
        N = len(board[0])
        
        
        for i in range(M):
            if board[i][0] == 'O':
                    magic(i,0)
            if board[i][N-1] == 'O':
                    magic(i,N-1)
                    
        for j in range(1,N-1):
            if board[0][j] == 'O':
                magic(0,j)
            if board[M-1][j] == 'O':
                magic(M-1,j)
        
        # print(board)
                
        for i in range(M):
            for j in range(N):
                if board[i][j] == -1:
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'