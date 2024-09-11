import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr) -> int:
       cost=0
       n=len(arr)
       heapq.heapify(arr)
       
       while len(arr)>1:
           first=heapq.heappop(arr)
           second=heapq.heappop(arr)
           new=first+second
           cost+=new
           heapq.heappush(arr,new)
       return cost
