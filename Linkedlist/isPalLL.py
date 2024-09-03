class Solution:
    def isPalindrome(self, head):
        slow,fast=head,head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        
        while slow:
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
        
        l,r=head,prev
        
        while r:
            if l.data!=r.data:
                return False
            r=r.next
            l=l.next
        return True
        
