class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        s=set()
        
        t=head
        while t:
            if t.data not in s:
                s.add(t.data)
                prev=t
            else:
                nxt=t.next
                prev.next=nxt
            t=t.next
            
        return head
