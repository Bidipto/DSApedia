# 725. Split Linked List in Parts

def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    res = []
    
    start = head 
    count = 0
    
    while start:
        start = start.next
        count += 1
        
    div = count//k
    extra = count%k
    print(div,extra)
    start = head 
    
    for i in range(k):
        pre = None 
        res.append(start)
        
        if not start:
            continue
            
        for j in range(div + min(max(extra,0),1)):
            if not pre:
                pre = start
            else:
                pre = pre.next
            start = start.next
                        
        if pre:
            pre.next = None 
        extra -= 1
    return res