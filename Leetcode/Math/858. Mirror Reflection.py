def mirrorReflection(self, N : int, size: int) -> int:
    side = True
    #right -> True, left-> False
    direction = True
    #up -> True, down -> False
    curr = N
    while True:
        # print(curr,side,direction)
        if direction:
            #case1 hitting 0
            if curr - size == 0:
                if side:
                    return 1
                else: 
                    return 2
            #case2: not hitting the top mirror
            elif curr - size>0:
                curr -= size
                side = not side
            #case3: hitting the top bar 
            else: 
                curr = -(curr-size)
                side = not side
                direction = not direction
        else:
            #case1 : hitting N
            if curr + size == N:
                if side:
                    return 0
                #this will never come true cause this will reach the intial state 
                #this case is useful if there exits no solution and we have to return - 1
                else: 
                    curr = N
                    side = not side
                    direction = not direction 
            #case2 : not hitting the bottom mirror
            elif curr + size<N:
                curr += size
                side = not side
            #case3 : hitting the mirror
            else: 
                curr = N-(curr+size-N)
                side = not side
                direction = not direction
            