from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        positiveDiag = set()
        negativeDiag = set()

        board = [["."]*n for i in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                # return board, e.g. if size n = 4 i.e. r should be 3 but its 4 coz it found solution
                b = ["".join(row) for row in board]
                res.append(b)
                return

            for c in range(n):
                if(c in cols):
                    continue
                if(r+c in positiveDiag):
                    continue
                if(r-c in negativeDiag):
                    continue

                # none of the case matches, so use the r,c and place queen
                board[r][c] = "Q"
                cols.add(c)
                positiveDiag.add(r+c)
                negativeDiag.add(r-c)

                backtrack(r+1)

                board[r][c] = "."
                cols.remove(c)
                positiveDiag.remove(r+c)
                negativeDiag.remove(r-c)

        backtrack(0)

        return res
