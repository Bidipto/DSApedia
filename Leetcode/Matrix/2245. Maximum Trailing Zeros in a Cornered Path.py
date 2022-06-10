# 2245. Maximum Trailing Zeros in a Cornered Path
# Such a bad and lenghty problem to solve, but the solution is very simple and elegant
# not so much of a elegant solution 
# the logic is to make a prefix sum array from up, down, left and right
# and the catch is we will store the nums of 2 and 5 factors in the prefix sum
# ie kinda factor sum with pairs
# adn the for each cell we will check the all the four ways that are posisble
# and keep track of the max
# the number of trailing zeros will be the min of no of 2 anf 5 factors in that path
class Solution:
    def get5(self,num):
        
        temp = 0
        while num%5==0:
            temp += 1
            num //= 5
        
        return temp
    
    def get2(self,num):
        # print(num, end = " ")
        temp = 0
        while num%2==0:
            temp += 1
            num //= 2
        # print(temp)
        return temp
    
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        dic = {}
        
        up = [[[0]*2 for w in range(N)] for q in range(M)]
        down = [[[0]*2 for w in range(N)] for q in range(M)]
        right = [[[0]*2 for w in range(N)] for q in range(M)]
        left = [[[0]*2 for w in range(N)] for q in range(M)]
        
        for i in range(M):
            for j in range(N):
                two = self.get2(grid[i][j])
                five = self.get5(grid[i][j])
                dic[(i,j)] = (two,five)
                
        for i in range(M):
            temp2 = 0
            temp5 = 0
            for j in range(N):
                two,five = dic[(i,j)]
                temp2 += two
                temp5 += five
                right[i][j][0] = temp2
                right[i][j][1] = temp5
                
            temp2 = 0
            temp5 = 0
            for j in range(N-1,-1,-1):
                two,five = dic[(i,j)]
                temp2 += two
                temp5 += five
                left[i][j][0] = temp2
                left[i][j][1] = temp5
                
        for j in range(N):
            temp2 = 0
            temp5 = 0
            for i in range(M):
                two,five = dic[(i,j)]
                temp2 += two
                temp5 += five
                down[i][j][0] = temp2
                down[i][j][1] = temp5
                
            temp2 = 0
            temp5 = 0
            for i in range(M-1,-1,-1):
                two,five = dic[(i,j)]
                temp2 += two
                temp5 += five
                up[i][j][0] = temp2
                up[i][j][1] = temp5
        
        res = 0    
        for i in range(M):
            for j in range(N):
                two,five = dic[(i,j)]
                # made a mistake of not removing the the factors of the currents cell in check
                # cause it will be counted twice
                res = max(res,min(up[i][j][0]+left[i][j][0]-two,up[i][j][1]+left[i][j][1]-five))           
                # if res == 4: print(i,j,"ul",up[i][j][0],left[i][j][0],up[i][j][1],left[i][j][1])
                res = max(res,min(up[i][j][0]+right[i][j][0]-two,up[i][j][1]+right[i][j][1]-five))         
                # if res == 4: print(i,j,"ur")
                res = max(res,min(down[i][j][0]+left[i][j][0]-two,down[i][j][1]+left[i][j][1]-five))       
                # if res == 4: print(i,j,"dl")
                res = max(res,min(down[i][j][0]+right[i][j][0]-two,down[i][j][1]+right[i][j][1]-five))     
                # if res == 4: print(i,j,"dr")
        return res
        
        
        
        
    