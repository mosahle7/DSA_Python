from typing import List


class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        ar=[]
        for i in range(n):
            a=[]
            a.append(arr[i])
            a.append(brr[i])
            a.append(abs(arr[i]-brr[i]))
            ar.append(a)
        
        ar.sort(key=lambda x:x[2], reverse=True)

        res=0
        for i in range(n):
            if x==0: 
                res+=ar[i][1]
                # y-=1


            elif y==0: 
                res+=ar[i][0]
                # x-=1

            else:
                if ar[i][0]>=ar[i][1]:
                    res+=ar[i][0]
                    x-=1
                else:
                    res+=ar[i][1]
                    y-=1
        return res
