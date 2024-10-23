class Solution:
    def sumOfLastN_Nodes(self, head, n):
        first,second=head,head
        
        for i in range(n):
            first=first.next
        
        while first is not None:
            first=first.next
            second=second.next
        
        s=0   
        while second is not None:
            s+=second.data
            second=second.next
        
        return s
            
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        l=0
        t=head
        while t is not None:
            l+=1
            t=t.next
        
        c=l-n
        s=0
        l=0
        t=head
        while t is not None:
            l+=1
            if l>c:
                s+=t.data
            t=t.next
        return s
        
        
