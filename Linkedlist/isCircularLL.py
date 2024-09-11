class Solution:
    def isCircular(self, head):
        if not head:  # If the list is empty, it's not circular
            return False
        
        # Start with the head
        current = head
        
        # Traverse the list and check if we loop back to the head
        while current.next:
            current = current.next
            # If we reach the head again, it's circular
            if current == head:
                return True
        
        # If we reach a node with `next` as None, it's not circular
        return False
