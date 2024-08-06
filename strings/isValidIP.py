class Solution:
    def isValid(self, str):
        li=str.split('.')
        
        n=len(li)
        if n!=4: return False
        
        for k in li:
            if not k.isdigit():
                return False
            if k[0]=='0' and k!='0':
                return False
            if not(0<=int(k)<=255):
                return False
        
        return True
