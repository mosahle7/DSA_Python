class Solution:
    def findSmallestMaxDist(self, stations, K):
        n=len(stations)
        left=0.0
        right = stations[n-1]-stations[0]

        def check(dist,n,stations,K):
            req=0
            for i in range(1,n):
                diff=stations[i]-stations[i-1]
                req+=int(diff/dist)

            return req<=K
        
        while right-left> 1e-6:
            mid=(left+right)/2.0

            if check(mid,n,stations,K):
                right=mid
            else:
                left=mid
        
        return round(right,2)
