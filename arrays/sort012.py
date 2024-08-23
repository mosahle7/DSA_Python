def sort012(arr, n) :

	# write your code here
    # don't return anything
    l,m,r=0,0,n-1

    while m<=r:
        if arr[m]==0:
            arr[m],arr[l]=arr[l],arr[m]
            m+=1
            l+=1
        elif arr[m]==1:
            m+=1
        else:
            arr[m],arr[r]=arr[r],arr[m]
            r-=1
    pass
