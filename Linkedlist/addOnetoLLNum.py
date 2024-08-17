class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
        
    def addOne(self, head):
        # Step 1: Reverse the linked list
        head = self.reverseList(head)
        
        # Step 2: Add one to the reversed list
        cur=head
        car=1
        
        while cur is not None:
            cur.data+=car
            
            if cur.data<10:
                car=0
                break
            else:
                cur.data=0
                car=1
            
            if cur.next is None and car>0:
                new=Node(1)
                cur.next=new
                car=0
            
            cur=cur.next
        
        # Step 3: Reverse the list back to original order
        head = self.reverseList(head)
        
        return head

class Solution:
    def addOne(self,head):
        num=0
        
        t=head
        m=0
        while t:
            m+=1
            t=t.next
            
        t=head
        while t:
            num+=((t.data)*(10**(m-1)))
            m-=1
            t=t.next
       
        num+=1
        l=len(str(num))
        
        head.data=(num//(10**(l-1)))
        num=num%(10**(l-1))
        l-=1
        
        t=head.next
        cur=head
        
        while l>0:
            if t is not None:
                t.data=(num//(10**(l-1)))
                num=num%(10**(l-1))
                l-=1
                cur=t
                t=t.next
            else:
                new=Node(num//(10**(l-1)))
                num=num%(10**(l-1))
                l-=1
                cur.next=new
                cur=new
        return head
