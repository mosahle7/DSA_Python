        
class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        original_start = start[:]  # Save the original sorted state of start
        n = len(start)
        
        def check(mid):
            for i in range(1, n):
                if start[i] - start[i-1] >= mid:
                    continue
                else:
                    if start[i] + d - start[i-1] < mid:
                        return False
                    start[i] = start[i-1] + mid
            return True
        
        l, r = 0, 2 * 10**9
        ans = 0
        
        while l <= r:
            mid = (l + r) // 2
            start = original_start[:]  # Reset start to the original state before each check
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans
