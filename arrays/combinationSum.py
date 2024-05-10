class Solution:
    def CombinationSum2(self, arr, n, k):
        arr.sort()
        res =[]
        
        def backtrack(start,path,target):

            if target<0:
                return
            
            if target == 0:
                res.append(path[:])
                return

            for i in range(start,n):

                if i>start and arr[i]==arr[i-1]:
                    continue
                
                path.append(arr[i])

                backtrack(i+1,path, target - arr[i])

                path.pop()

        backtrack(0,[])
        return res
