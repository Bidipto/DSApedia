# 475. Heaters

def findRadius(self, houses: List[int], heater: List[int]) -> int:
    #for each house we need the closest left and closedt right heater,
    #and store them 
    #to edge cases when no left or no right ie at the begining and the end 

    houses.sort()
    heater.sort()
    i = 0
    res = 0 
    N = len(heater)

    for house in houses:
        while i+1<N and heater[i+1]<=house:
            i += 1

        if i == 0 and heater[i]>house:
            #no heater to the left 
            res = max(res,heater[i]-house)
        elif i == N - 1 and heater[i]<=house:
            res = max(res,house-heater[i])
        else:
            res = max(res,min(heater[i+1]-house,house-heater[i]))

    return res