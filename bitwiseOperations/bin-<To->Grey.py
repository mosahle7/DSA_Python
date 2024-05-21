class Solution:
  def binToGray(self,B):
    l=len(B)
    n=int(B,2)
    return (bin(n^(n>>1))[2:]).zfill(l)

  def grayToBin(self,G):
    l=len(G)
    n=int(G,2)
    res=n
    while n>0:
      n>>=1
      res^=n
    return (bin(res)[2:]).zfill(l)
      
