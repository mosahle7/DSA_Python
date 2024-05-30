
def intersetPoint(h1,h2):
        if not h1 or not h2: return None
        p1,p2= h1,h2
        while p1!=p2: 
            p1=p1.next if p1 else h2
            p2=p2.next if p2 else h1
        
        return p1.data if p1 else -1

    
