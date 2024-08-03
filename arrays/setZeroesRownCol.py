class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        
        row=set()
        col=set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        
        for k in row:
            for j in range(n):
                matrix[k][j]=0
        
        for k in col:
            for i in range(m):
                matrix[i][k]=0
        return matrix
            
class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        m,n=len(mat),len(mat[0])
        
        firstRowHas0s=any(mat[0][j]==0 for j in  range(n))
        firstColHas0s=any(mat[i][0]==0 for i in range(m))
        
        for i in range(1,m):
            for j in range(1,n):
                if mat[i][j]==0:
                    mat[i][0]=0
                    mat[0][j]=0
                    
        for i in range(1,m):
            for j in range(1,n):
                if mat[i][0]==0 or mat[0][j]==0:
                    mat[i][j]=0
                    
        if firstRowHas0s:
            for j in range(n):
                mat[0][j]=0
        if firstColHas0s:
            for i in range(m):
                mat[i][0]=0
