class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        slow,fast=head,head
        while True:
            if not(fast) or not(fast.next): return False
            slow=slow.next
            fast=fast.next.next
            if slow==fast: return True
            
