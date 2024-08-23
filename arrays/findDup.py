
def findDuplicate(arr:list, n:int):
    # Write your code here.
    # Returns an integer.
    s=set()
    for i in arr:
        if i in s: return i
        if i not in s: s.add(i)


def findDuplicate(arr:list, n:int):
    slow,fast=arr[0],arr[0]

    while True:
        slow=arr[slow]
        fast=arr[arr[fast]]
        if slow==fast: break
    
    slow=arr[0]
    while slow!=fast:
        slow=arr[slow]
        fast=arr[fast]
    
    return slow
