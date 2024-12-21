
class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        n=len(mat)
        for i in range(n):
            for j in range(i,n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        for i in range(n//2):
            mat[i],mat[n-1-i]=mat[n-1-i],mat[i]
