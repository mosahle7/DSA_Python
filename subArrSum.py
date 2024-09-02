def subArrSum(arr,tar):
    n=len(arr)
    ans=[]
    def fun(i,sum,path):
        
        if sum==tar: 
            ans.append(path)
            return

        if i==n: 
            return

        if sum+arr[i]<=tar:
            # path.append(arr[i])
            fun(i+1,sum+arr[i],path+[arr[i]])
            # path.pop()
        
        fun(i+1,sum,path)
        return

    fun(0,0,[])
    return ans
