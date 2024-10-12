from collections import deque

def longStrAB(AA,BB,AB):
    st=deque([])
    while AA>0 or BB>0 or AB>0:
        if len(st)<1:
            if AA>=BB and AA>0:
                st.append('AA')
                AA-=1
            elif BB>AA and BB>0:
                st.append('BB')
                BB-=1
            elif AB>0:
                st.append('AB')
                AB-=1
        else:
            if st[-1][1]=='B' and AA>0:
                st.append('AA')
                AA-=1
            elif st[-1][1]=='A' and BB>0:
                st.append('BB')
                BB-=1
            elif st[-1][1]=='B' and AB>0:
                st.append('AB')
                AB-=1
            else: break
    
    
    while AB>0 and st[0][0]=='A':
        st.appendleft('AB')
        AB-=1
        
    i=0
    l=len(st)
    
    while AB>0 and i<l-1:
        l=len(st)
        if st[i][1]=='B' and st[i+1][0]=='A':
            st.appendleft('AB')
            AB-=1
            i+=1
    while AB>0 and st[-1][1]=='B':
        st.append('AB')
        AB-=1

    return ''.join(st)
