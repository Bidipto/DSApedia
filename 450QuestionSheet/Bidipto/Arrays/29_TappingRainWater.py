#first we traverse from left to right and keep track of the largest height upto that
#then from right to left and keep track of the largest height upto that
#now we know for each index, the largest height we can get from left and right
#and since the water will spill we need the minimum of both sides
def trappingWater(self, height,n):
    left=[]
    right=[]
    left.append(0)
    right.append(0)
    high=0
    water=0
    for i in range(len(height)-1):
        high=max(high,height[i])
        left.append(high)
    high=0
    for i in range(len(height)-1,0,-1):
        high=max(high,height[i])
        right.append(high)
    #print(left,right)
    for i in range(len(height)):
        level=min(left[i],right[len(height)-i-1])
        if level>height[i]:
            temp=level-height[i]
            water+=temp
        #print(i,level,left[i],right[len(height)-i-1])
    return water