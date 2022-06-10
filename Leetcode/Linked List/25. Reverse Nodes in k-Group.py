# 25. Reverse Nodes in k-Group
# k = 3 for example:

# step 0: pre -> a -> b -> c -> (next k-group)

# step 1: pre ->     b -> c -> (next k-group)
#                         a ---^

# step 2: pre ->          c -> (next k-group)
#                    b -> a ---^

# step 3: pre ->               (next k-group)
#               c -> b -> a ---^

# finish: pre -> c -> b -> a -> (next k-group)
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head 
        #pre will always give the last node of the last group
        pre = dummy 
        left,right = head,head
        
        while True:
            count = 0
            while right and count<k:
                count += 1
                right = right.next
            # print(right.val)
            if count == k:
                #first is the first element of the current k group
                first = left 
                #last is thr first element of the next k group
                last = right
                #here we put one node after the other behind the back of last
                #and move the first forward
                for q in range(k):
                    temp = first.next
                    first.next = last
                    last = first
                    first = temp 
                
                pre.next = last 
                pre = left
                left = right
                
            else:
                return dummy.next