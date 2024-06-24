
class Solution:
    def sumMatrix(self, n: int, q: int) -> int:
        if q < 2 or q > 2 * n:
            return 0
        
        # Calculate the number of occurrences of q in the matrix
        # q will appear (q - 1) times in the matrix
        if q <= n:
            return q - 1
        else:
            return 2 * n - q + 1
