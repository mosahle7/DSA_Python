#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix): 
        ans=[]
        i=0
        j=0
        m=len(matrix)
        n=len(matrix[0])
        s=set()
        ele=0
        dir=0
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        while ele<(m*n):
            
            if (i,j) not in s:
                ans.append(matrix[i][j])
                ele+=1
                s.add((i,j))
            else:
                i-=dx[(dir%4)]
                j-=dy[(dir%4)]
                dir+=1

            i+=dx[(dir%4)]
            j+=dy[(dir%4)]
            

            if j<0 or j>=n or i<0 or i>=m: 
                i-=dx[(dir%4)]
                j-=dy[(dir%4)]
                dir+=1
                i+=dx[(dir%4)]
                j+=dy[(dir%4)]
        return ans
        
#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix): 
        ans=[]
        i=0
        j=0
        m=len(matrix)
        n=len(matrix[0])
        
        top,bottom,left,right = 0,m-1,0,n-1
        
        while top<=bottom and left<=right:
            
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top+=1
            
            for j in range(top,bottom+1):
                ans.append(matrix[j][right])
            right-=1
            
            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1
            if left<=right:
                for j in range(bottom,top-1,-1):
                    ans.append(matrix[j][left])
                left+=1
        
        return ans
            
            
                
            
            

