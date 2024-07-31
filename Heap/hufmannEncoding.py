import heapq

class Node:
    def __init__(self,char=None,freq=None):
        self.char=char
        self.freq=freq
        self.left=None
        self.right=None
    
    def __lt__(self,other):
        return self.freq<other.freq

class Solution:
    def huffmanCodes(self,S,f,N):
        minHeap=[]
        nodes=[]
        for char,freq in zip(S,f):
            nodes.append(Node(char,freq))
        
        for node in nodes:
            heapq.heappush(minHeap, node)

        eles=[]
        while len(minHeap)>1:
            left=heapq.heappop(minHeap)
            right=heapq.heappop(minHeap)
            newNode=Node(None,left.freq+right.freq)
            newNode.left=left
            newNode.right=right

            heapq.heappush(minHeap,newNode)
        #     eles.append([(x.char,x.freq) for x in minHeap])
        # elees=[]
        # return eles

        ans=[]

        root=heapq.heappop(minHeap)

        # root.left.freq='0'
        # root.right.freq='1'

        def pre(node,s):
            if not(node):
                return
            node.freq=s
            if node.char:
                ans.append(node.freq)
            pre(node.left,s+'0')
            pre(node.right,s+'1')
            return 

        pre(root,'')
        return ans

S = "abcdef"
f = [5, 9, 12, 13, 16, 45]
N=6
ob=Solution()
print(ob.huffmanCodes(S,f,N))
