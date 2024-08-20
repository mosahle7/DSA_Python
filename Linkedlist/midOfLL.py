class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        if not(head): return -1
        
        n=0
        t=head
        while t:
            n+=1
            t=t.next
        
        m=n//2+1
        k=0
        t=head
        while k!=m-1:
            k+=1
            t=t.next
        
        return t.data

class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        if not(head): return -1
        
        slow,fast=head,head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        return slow.data
