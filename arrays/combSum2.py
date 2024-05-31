class Solution:
    
    def CombinationSum2(self, arr, n, k):
        res=[]
        arr.sort()
        def dfs(ind,n,k,path):
            if k<0: return
            if k==0: 
                res.append(path[:])
            if ind==n: return

            for i in range(ind,n):
                if i>ind and arr[i]==arr[i-1]: continue
                path.append(arr[i])
                dfs(i+1,n,k-arr[i],path)
                path.pop()
        dfs(0,n,k,[])
        return res
