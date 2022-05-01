# solved cherry pick up 2 first so i feel 2 was more 1 and 1 is more 2
# the logic is hard to come up with
#the monopoly of this logic is if we keep moveing two robots from [0][0]
#we will for sure reach the end in the same time
#also the logic to start both the robots at the same time.
def cherryPickup(self, arr: List[List[int]]) -> int:
    # N x N grid
    N = len(arr)
    dp = {}
    
    def magic(m1,n1,m2,n2):
        #1 and 2 will always reach the end at the same 
        #since only right and down movement is allowed
        if m1 == N-1 and n1 == N-1:
            return arr[m1][n1]
        
        #out of bounds and thorn check
        if n1 == N or m1 == N or n2 == N or m2 == N or arr[m1][n1] == -1 or arr[m2][n2] == -1:
            return -1
        #memo check 
        if (m1,n1,m2,n2) in dp:
            return dp[(m1,n1,m2,n2)]
        
        #number of cherry check
        #if they are one the same cell we can only pick once
        if n1 == n2 and m1 == m2:
            cherry = arr[m1][n1]
        else:
            cherry = arr[m1][n1] + arr[m2][n2]
        
        temp = max( magic(m1+1,n1,m2+1,n2),  #down,down
                    magic(m1,n1+1,m2+1,n2),     #right,down
                    magic(m1+1,n1,m2,n2+1),    #down,right
                    magic(m1,n1+1,m2,n2+1)       #right.right
        )
        
        # if we return a - inf instead of a -1 we could have avoided this check
        if temp != -1:
            dp[(m1,n1,m2,n2)] = cherry + temp
        else: 
            dp[(m1,n1,m2,n2)] = -1
        return dp[((m1,n1,m2,n2))]
    
    return max(magic(0,0,0,0),0)