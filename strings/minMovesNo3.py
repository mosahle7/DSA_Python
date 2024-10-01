def abab(s):
    n=len(s)
    moves=0
    m=0
    k=s[0]
    m=1
    for i in range(1,n):
        if s[i]==k:
            m+=1
            
        else:
            if m>=3:
                moves+=m//3
            m=1
            k=s[i]
    if m>=3: moves+=m//3
    
    return moves

s="baaabbaabbba"
print(abab(s))
            
            
        
