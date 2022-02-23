from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:

        self.R = len(board)
        self.C = len(board[0])

        def dfs(i, j, visited, wordTillNow):
            # check if i and j are in bounds
            print(wordTillNow)
            if((i, j) in visited):
                print("VISITED ", board[i][j])
                return False

            if(i < 0 or j < 0 or i >= self.R or j >= self.C):
                return False

            print(board[i][j])

            wordTillNow = wordTillNow + board[i][j]

            if(len(wordTillNow) > len(word)):
                return False

            if(word[:len(wordTillNow)] != wordTillNow):
                return False

            if(wordTillNow == word):
                return True

            visited.add((i, j))

            return dfs(i+1, j, visited, wordTillNow) or dfs(i-1, j, visited, wordTillNow) or dfs(i, j+1, visited, wordTillNow) or dfs(i, j-1, visited, wordTillNow)

        for r in range(self.R):
            for c in range(self.C):
                if(dfs(r, c, set(), "")):
                    return True

        return False


board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
word = "ABCESEEEFS"

print(Solution().exist(board, word))
