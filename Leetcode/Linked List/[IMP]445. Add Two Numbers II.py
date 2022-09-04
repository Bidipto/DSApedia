# compared the length of the lls and then added nodes with value zero in front of the smaller ll
# then did a recurion with a carry 

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        M = self.count(l1)
        N = self.count(l2)
        
        if M>N:
            l2 = self.addZero(M-N,l2)
        elif N>M:
            l1 = self.addZero(N-M,l1)
        
        dummy = ListNode(1)
        dummy.next = l1
        
        carry = self.magic(l1,l2)
        
        if not carry: return dummy.next
        else: return dummy
        
    def magic(self,l1,l2):
            if not l1:
                return 0
            
            c = self.magic(l1.next,l2.next)
            
            c,l1.val = divmod((l1.val+l2.val+c),10)  
            
            return c
    
    def count(self, head):
        if not head: return 0
        else: return 1 + self.count(head.next)
        
    def addZero(self, num, head):
        dummy = ListNode(-1)
        pre = dummy 
        for i in range(num):
            temp = ListNode(0)
            pre.next = temp 
            pre = temp
            
        pre.next = head 
        return dummy.next