# https://leetcode.com/discuss/interview-question/347457

class Solution:

    def makeMove(self, curPos):
        """
        Handles dangerous moves and unreachable states.
        """
        possibleMoves = {
            'up': (curPos[0]-1, curPos[1]),
            'down': (curPos[0]+1, curPos[1]),
            'left': (curPos[0], curPos[1]-1),
            'right': (curPos[0], curPos[1]+1)
        }

        finalMoves = []
        for i in possibleMoves:
            if possibleMoves[i][0] < 0 or possibleMoves[i][0] >= self.matrix_rows or possibleMoves[i][1] < 0 or possibleMoves[i][1] >= self.matrix_cols:
                # possibleMoves.pop(i)
                continue

            if self.matrix[possibleMoves[i][0]][possibleMoves[i][1]] == "D":
                continue
            finalMoves.append(possibleMoves[i])

        return finalMoves

    def treasureIsland(self, matrix, st=[(0, 0)]):
        """
        O are safe to traverse
        X is the goal state
        D is dangerous
        """
        self.matrix = matrix
        self.matrix_rows = len(matrix)
        self.matrix_cols = len(matrix[0])
        # st = (0, 0)

        remainingmMoves = st
        visited = set()
        step = 0
        while remainingmMoves:
            nextMoves = []
            for move in remainingmMoves:
                if move in visited:
                    continue
                visited.add(move)
                if self.matrix[move[0]][move[1]] == "X":
                    return step
                nextMoves += self.makeMove(move)
            remainingmMoves = nextMoves
            step += 1

        return -1

    def treasureIsland2(self, matrix):
        """
        O are safe to traverse
        X is the goal state
        D is dangerous
        S is the start states
        """
        start_states = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "S":
                    start_states.append((i, j))
        return self.treasureIsland(matrix, start_states)


# matrix = [['O', 'O', 'O', 'O'],
#           ['D', 'O', 'D', 'O'],
#           ['O', 'O', 'O', 'O'],
#           ['X', 'D', 'D', 'O']]


# print(Solution().treasureIsland(matrix))

matrix = [['S', 'O', 'O', 'S', 'S'],
          ['D', 'O', 'D', 'O', 'D'],
          ['O', 'O', 'O', 'O', 'X'],
          ['X', 'D', 'D', 'O', 'O'],
          ['X', 'D', 'D', 'D', 'O']]

print(Solution().treasureIsland2(matrix))
