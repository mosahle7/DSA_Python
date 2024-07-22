def removeDuplicates(head):
    t=head.data
    while head.next:
        if head.next.data == t:
            head.next=head.next.next
        else:
            head=head.next
            t=head.data
        
    return head
    
