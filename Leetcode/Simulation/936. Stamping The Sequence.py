# 936. Stamping The Sequence

def movesToStamp(self, stamp: str, target: str) -> List[int]:
    #we have to start from the end and then move backwards
    pattern = set()
    N = len(stamp)
    
    for i in range(N):
        for j in range(i+1,N+1):
            pattern.add("#"*i + stamp[i:j] + "#"*(N-j))
            
    # print(pattern)
    
    test = "#"*len(target)
    res = []
    
    while target != test:
        flag = False 
        for i in range(len(target)-N+1):
            # print(target[i:i+N])
            if target[i:i+N] in pattern:
                res.append(i)
                target = target[:i] + '#'*N + target[i+N:]
                flag = True 
        if not flag: return []
        
    return res[::-1]
        