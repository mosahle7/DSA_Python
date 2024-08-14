class Solution:
    def wordBreak(self, n, dict, s):
        d = set(dict)  # Convert the list to a set for O(1) lookups
        memo = {}  # Dictionary to store results for memoization
        l = len(s)
        
        def fun(i):
            if i in memo:
                return memo[i]
            
            if i == l:
                return [""]  # Base case: return a list with an empty string
            
            sub = ''
            results = []
            
            for j in range(i, l):
                sub += s[j]
                if sub in d:
                    subsequent_results = fun(j + 1)
                    for result in subsequent_results:
                        if result:
                            results.append(sub + " " + result)
                        else:
                            results.append(sub)
            
            memo[i] = results  # Store results in memoization dictionary
            return results
        
        return fun(0)


class Solution:
    def wordBreak(self, n, dict, s):
        ans=[]
        l=len(s)
        d=set()

        for i in range(n):
            d.add(dict[i])
            
        if s in d:
            if len(d)==1: return [s]
            else: ans.append(s)
        
        def fun(i,st):
            if i==l: return 1
            
            sub=''
            for j in range(i,l):
                sub+=s[j]
                if sub in d and fun(j+1,st+' '+sub if len(st)!=0 else st+sub)==1:
                    if st!="":
                        a=st+' '+sub
                        ans.append(a)
            return 0
        fun(0,'')
        return ans
