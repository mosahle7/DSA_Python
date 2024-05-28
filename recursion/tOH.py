class Solution:
    def toh(self, N, A, C, B):
        if N==1:
            print("move disk 1 from rod",A, "to rod",C)
            return 2**N-1
        self.toh(N-1,A,B,C)
        print("move disk",N,"from rod",A,"to rod",C)
        self.toh(N-1,B,C,A)
        return 2**N-1
