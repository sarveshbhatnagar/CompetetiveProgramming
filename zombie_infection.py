class Solution:

    def getLocations(self, pos, matrix_row, matrix_col, notInfected):
        locations = []
        vals = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }
        for i in vals:
            new_pos = (pos[0] + vals[i][0], pos[1] + vals[i][1])
            if new_pos[0] < 0 or new_pos[0] >= matrix_row or new_pos[1] < 0 or new_pos[1] >= matrix_col:
                continue
            if new_pos in notInfected:
                locations.append(new_pos)
        return locations

    def timeToZombify(self, matrix):
        # Get positions of infected zombies
        infected = []
        notInfected = set()
        matrix_row = len(matrix)
        matrix_col = len(matrix[0])
        for i in range(matrix_row):
            for j in range(matrix_col):
                if matrix[i][j] == 1:
                    infected.append((i, j))
                else:
                    notInfected.add((i, j))

        count = 0

        while len(infected) > 0:
            new_infected = []
            for pos in infected:
                locations = self.getLocations(
                    pos, matrix_row, matrix_col, notInfected)
                for location in locations:
                    notInfected.remove(location)
                new_infected.extend(locations)
            infected = new_infected
            count += 1
        return count-1


matrix = [[0, 1, 1, 0, 1],
          [0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 1, 0, 0, 1]]

print(Solution().timeToZombify(matrix))
