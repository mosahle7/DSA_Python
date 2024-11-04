def findLargestMinDistance(boards:list, k:int):
    # Write your code here
    # Return an integer
    n=len(boards)
    def canSplit(maxS):
        subCnt=1
        cSum=0

        for num in boards:
            if cSum+num>maxS:
                subCnt+=1
                cSum=num

                if subCnt>k: return False
            else:
                cSum+=num
        return True

    l,r=max(boards),sum(boards)

    while l<=r:
        mid=(l+r)//2

        if canSplit(mid):
            res=mid
            r=mid-1
        else:
            l=mid+1

    return res
