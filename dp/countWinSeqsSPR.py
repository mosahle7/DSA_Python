class Solution:
    def countWinningSequences(self, st: str):
        n = len(st)
        moves = ['F', 'W', 'E']
        memo = {}
        m=10**9+7

        def fun(i, l,d):
            # If this state has already been computed, return the stored result
            if (i, l, d) in memo:
                return memo[(i, l, d)]

            # Base case: all rounds are complete
            if i == n:
                if d>0:
                    return 1  # Bob wins in this sequence
                else:
                    return 0  # Bob doesn't win in this sequence

            # Prune the search if Bob can't catch up
            # if d + (n - i - 1) < 0:
            #     return 0

            # Try all valid moves for Bob
            count = 0
            for k in range(3):
                if moves[k] == l:
                    continue  # Bob can't use the same move as the last one
                
                # Calculate scores based on Alice's move
                p=0
                if st[i] == 'F':
                    if moves[k] == 'W':
                        p += 1
                    if moves[k] == 'E':
                        p -= 1
                elif st[i] == 'W':
                    if moves[k] == 'E':
                        p += 1
                    if moves[k] == 'F':
                        p -= 1
                else:  # Alice summoned 'E'
                    if moves[k] == 'F':
                        p += 1
                    if moves[k] == 'W':
                        p -= 1
                
                # Recursive call with the new state and accumulate the result
                count += fun(i + 1, moves[k], d+p)

            # Memoize the result of this state
            memo[(i, l, d)] = count
            return count

        # Start the recursive function
        return fun(0, '', 0)%m

class Solution:
    def countWinningSequences(self, s: str) -> int:
        n = len(s)
        NP = 0
        MOD = 10**9 + 7
        
        # Initialize the DP table
        dp = [[[NP for _ in range(4)] for _ in range(2 * n + 1)] for _ in range(n + 1)]
        
        moves = ['F', 'W', 'E']

        # Define the winner function
        def winner(alice: str, bob: int) -> int:
            aliceIdx = moves.index(alice)
            if aliceIdx == bob:
                return 0
            if aliceIdx == (bob + 1) % 3:
                return -1
            if (aliceIdx + 1) % 3 == bob:
                return 1
            assert False

        dp[0][n][3] = 1  # Base case

        for i in range(n):
            for w in range(2 * n + 1):
                for last in range(4):
                    if dp[i][w][last] == NP:
                        continue
                    for ll in range(3):
                        if ll == last:
                            continue
                        ii = i + 1
                        ww = w + winner(s[i], ll)
                        dp[ii][ww][ll] = (dp[ii][ww][ll] + dp[i][w][last]) % MOD

        ans = 0
        for w in range(n + 1, 2 * n + 1):
            for l in range(3):
                ans = (ans + dp[n][w][l]) % MOD

        return ans
