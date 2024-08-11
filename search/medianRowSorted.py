
class Solution:
    def median(self, matrix, R, C):
                                            
                         
        def upperBound(arr, x, n):
            low = 0
            high = n - 1
            ans = n

            while low <= high:
                mid = (low + high) // 2
        # maybe an answer
                if arr[mid] > x:
                    ans = mid
            # look for a smaller index on the left
                    high = mid - 1
                else:
                    low = mid + 1  # look on the right

            return ans

        def countSmallEqual(matrix, m, n, x):
            cnt = 0
            for i in range(m):
                cnt += upperBound(matrix[i], x, n)
            return cnt

        low = float('inf')
        high = float('-inf')

    # point low and high to the right elements
        for i in range(R):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][C - 1])

        req = (R*C) // 2
        while low <= high:
            mid = (low + high) // 2
            smallEqual = countSmallEqual(matrix, R, C, mid)
            if smallEqual <= req:
                low = mid + 1
            else:
                high = mid - 1

        return low
