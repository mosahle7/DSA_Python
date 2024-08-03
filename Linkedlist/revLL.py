class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        
        stack=[]
        
        while temp is not None:
            stack.append(temp.val)
            temp=temp.next
            
        temp=head
        
        while stack:
            value=stack.pop()
            temp.val=value
            temp=temp.next
            
        return head



class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        prev=None
        while cur is not None:
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
            
        return prev
