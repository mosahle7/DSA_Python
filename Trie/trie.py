from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

class TrieNode:
    def __init__(self):

        self.links=[None]*26
        self.flag=False

    def containsKey(self,ch):
        return self.links[ord(ch)-ord('a')] is not None

    def put(self,ch,node):
        self.links[ord(ch)-ord('a')]=node
    
    def get(self,ch):
        return self.links[ord(ch)-ord('a')]

    def setEnd(self):
        self.flag=True
    
    def isEnd(self):
        return self.flag

class Trie :

    def __init__(self) :
        self.root=TrieNode()

    
    def insert(self, string) :
        node=self.root
        for i in range(len(string)):
            if not(node.containsKey(string[i])):
                node.put(string[i],TrieNode())
            # moves to reference trie
            node=node.get(string[i])
                
        node.setEnd()


    
    def search(self, word) :
        node=self.root
        for i in range(len(word)):
            if not(node.containsKey(word[i])):
                return False
            node=node.get(word[i])
        return node.isEnd()
        
    def startWith(self, prefix) :
        node=self.root
        for i in range(len(prefix)):
            if not(node.containsKey(prefix[i])):
                return False
            node=node.get(prefix[i])
        return True

