#kinda cheating 
#not actually seapping the nodes but just the values
#we reach the left node using a for loop and since we dont know how long the ll is
#and we already have left (ie the k th node from start)
#we use this info to reach the kth node form end
def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    left = head
    for i in range(k-1):
        left = left.next
    
    right = head
    temp = left
    while temp.next:
        right = right.next
        temp = temp.next
        
    right.val,left.val = left.val,right.val
    return head

#the not cheating way of actually swappin the node
#used dummy nodes cause what of k is 1 
def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = head
        right = head 
        dummy = ListNode
        dummy.next = head
        dummy.val = 0
        prev_left = dummy
        prev_right = dummy
        for i in range(k-1):
            left = left.next
            prev_left = prev_left.next
        
        temp = left
        while temp.next:
            right = right.next
            temp = temp.next
            prev_right = prev_right.next
        
        # print(left.val,right.val,prev_left.val,prev_right.val)
        prev_left.next = right
        prev_right.next = left
        right.next,left.next = left.next,right.next
        #returned head initially but later realised that what id head is swapped
        #aaj ka siksha
        #create a dummy and return dummy.next always
        return dummy.next