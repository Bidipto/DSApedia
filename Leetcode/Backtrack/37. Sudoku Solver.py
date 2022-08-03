from collections import defaultdict,deque
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        test = set([str(i) for i in range(1,10)])
        col = defaultdict(set)
        row = defaultdict(set)
        sq = defaultdict(set)
        que = deque()
        
        for i,j in product(range(9),range(9)):
            
            if board[i][j] == ".":
                que.append((i,j))
            else:    
                val = board[i][j]

                row[i].add(val)
                col[j].add(val)
                sq[(i//3,j//3)].add(val)
        
        def magic():
            if not que:
                return True
            i,j = que[0]
            # print(i,j,test-row[i]-col[j]-sq[(i//3,j//3)],row[i],col[j],sq[(i//3,j//3)])
            for val in test:
                if val not in row[i] and val not in col[j] and val not in sq[i//3,j//3]:
                    # print(i,j,val)
                    board[i][j] = str(val)

                    row[i].add(val)
                    col[j].add(val)
                    sq[(i//3,j//3)].add(val)
                    que.popleft()

                    if magic():
                        return True

                    else:

                        row[i].discard(val)
                        col[j].discard(val)
                        sq[(i//3,j//3)].discard(val)
                        que.appendleft((i,j))
            
        magic()