class Solution:

    def moveRobot(self, matrix, current_position):
        """
        Handles following cases:
        if moving results in 0 no result
        otherwise returns positions.
        """
        # move robot to the right
        # or down
        down_move = current_position[0] + \
            1, current_position[1], current_position[2] + 1
        right_move = current_position[0], current_position[1] + \
            1, current_position[2] + 1
        if not down_move[0] < len(matrix):
            # invalid down move
            down_move = current_position
        if not right_move[1] < len(matrix[0]):
            # invalid right move
            right_move = current_position

        # check if 0 pos...
        moves = [down_move, right_move]
        answers = []
        for move in moves:
            if(matrix[move[0]][move[1]] != 0 and move != current_position):
                answers.append(move)
        return answers

    def demolitionRobot(self, matrix):
        # robot can only make right moves
        # or down moves.
        positions = [(0, 0, 0)]
        while len(positions) > 0:
            current_position = positions.pop()
            new_pos = self.moveRobot(matrix, current_position)
            # check if there is 9 in new positions.
            for pos in new_pos:
                if(matrix[pos[0]][pos[1]] == 9):
                    return pos[2]

                # add new positions to the list.
                positions.append(pos)

        return -1


matrix = [[1, 0, 0], [1, 0, 0], [1, 1, 9]]
print(Solution().demolitionRobot(matrix))
