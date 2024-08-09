def rightRot(s1,s2):
    return len(s1)==len(s2) and s2 in s1+s1
    
s1="ahles"
s2="sahle"
print(rightRot(s1,s2))
