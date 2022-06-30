# 234. Palindrome Linked List

def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.head = head 
        
        def magic(node):
            
            if node.next:
                res = magic(node.next)
                if not res:
                    return False 
                
            if node.val != self.head.val:
                return False 
            
            self.head = self.head.next
            
            return True
        
        return magic(head)