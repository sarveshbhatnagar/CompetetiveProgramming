class Solution:

    def isValid(self, pos):
        if(pos[0] >= self.matrix_row or pos[1] >= self.matrix_col):
            return False
        return True

    def get_all_path_to_goal(self, matrix, st):
        self.matrix_row = len(matrix)
        self.matrix_col = len(matrix[0])
        self.matrix = matrix

        pos = st
        goal = self.matrix_row-1, self.matrix_col-1
        self.path = []

        self.make_move(pos[0], goal, [])
        self.make_move(pos[1], goal, [])

        return self.path

    def make_move(self, pos, goal, path):
        if pos == goal:
            print(path)
            self.path.append(path)

            return True

        # explore
        path.append(self.matrix[pos[0]][pos[1]])

        # Down move
        np = pos[0]+1, pos[1]
        if self.isValid(np):
            npp = path.copy()
            self.make_move(np, goal, npp)

        # Right move
        np = pos[0], pos[1]+1
        if self.isValid(np):
            npp = path.copy()
            self.make_move(np, goal, npp)

        return False


matrix = [[1, 2, 3],
          [4, 5, 1]]


print(Solution().get_all_path_to_goal(matrix, [(0, 1), (1, 0)]))
