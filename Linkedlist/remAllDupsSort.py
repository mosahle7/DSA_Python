class Solution:
    def removeAllDuplicates(self, head):
        dummy=Node(0)
        dummy.next=head
        prev=dummy
        while head:
            if head.next and head.data==head.next.data:
                while head.next and head.data==head.next.data:
                    head=head.next
                prev.next=head.next
            else:
                prev=prev.next
            head=head.next
            
        return dummy.next
