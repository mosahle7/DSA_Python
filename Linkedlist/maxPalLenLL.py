class Solution:
    def maxPalindrome(self, head) -> int:
        if head is None: 
            return 0
        if head.next is None: 
            return 1
        
        def cs(a,b):
            c=0
            while a and b and a.data==b.data:
                a=a.next
                b=b.next
                c+=1
            return c
        cur=head
        ans=1
        prev=None
        
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
            
            ans=max(ans,cs(prev,cur)*2)
            
            if cur: ans=max(ans,cs(prev,cur.next)*2+1)
        return ans
