from collections import defaultdict

def maxPathSumTree(n, par, values):
    adj=defaultdict(list)
    for i in range(1,n):
        adj[par[i]].append(i)
        adj[i].append(par[i])
    
    maxSum=float('-inf')
    def dfs(i,sum,mSum,vis):
        vis[i]=True
        for k in adj[i]:
            if vis[k]==True:
                continue
            sum=sum+values[k]
            mSum=max(mSum,sum)
            mSum=dfs(k,sum,mSum,vis)
        return mSum

    for i in range(n):
        vis=[False]*(n)
        maxSum=max(maxSum,dfs(i,values[i],values[i],vis))
    return maxSum


# Example usage
n = 5
parent = [-1, 0, 1, 2, 0]
values = [-2, 10, 12, -4, 7]
print(maxPathSumTree(n, parent, values))  # Output should be the maximum path sum


from collections import defaultdict

def maxPathSumTree(n, par, values):
    adj = defaultdict(list)
    for i in range(1, n):
        adj[par[i]].append(i)
        adj[i].append(par[i])
    
    def dfs(node, parent):
        nonlocal maxSum
        current_sum = values[node]
        max_child_sum = 0
        sum_child_sum=0
        for neighbor in adj[node]:
            if neighbor == parent:
                continue
            subtree_sum = dfs(neighbor, node)
            if subtree_sum > 0:
                child_sum = subtree_sum
                sum_child_sum += child_sum
                max_child_sum = max(max_child_sum, child_sum)

        maxSum = max(maxSum, current_sum + sum_child_sum)
        return max(0, current_sum + max_child_sum)
