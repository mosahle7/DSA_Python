class Solution:
    def delete_node(self, head, x):
        if x==1:
            if head.next:
                head.next.prev=None 
                head=head.next
            else: head=None
            return head
        m=2
        n=head.next
        while n:
            if m==x:
                if n.next:
                    n.prev.next=n.next
                    n.next.prev=n.prev
                else:
                    n.prev.next=None
                return head
            n=n.next
            m+=1
                
