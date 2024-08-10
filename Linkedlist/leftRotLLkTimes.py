class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        if k==0: return head
        
        cur=head
        c=head
        count=0
        
        while cur:
            count+=1
            cur=cur.next
        
        k=k%count
        if k==0:
            return head
            
        cur=head

        for i in range(1,k+1):
            if i==k:
                newHead=cur.next
                cur.next=None
                break
            
            cur=cur.next
            
        head=newHead
        while newHead.next:
            newHead=newHead.next
            
        newHead.next=c
        
        return head
        
        
