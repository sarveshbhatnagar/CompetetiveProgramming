from shutil import move


def processCommand(currPos, command):
    r = currPos[0]
    c = currPos[1]
    if command == "UP":
        r = currPos[0] - 1
        c = currPos[1]
    if command == "DOWN":
        r = currPos[0] + 1
        c = currPos[1]
    if command == "LEFT":
        r = currPos[0]
        c = currPos[1] - 1
    if command == "RIGHT":
        r = currPos[0]
        c = currPos[1] + 1
    if r < 0 or c < 0:
        return currPos
    return r, c


def convertPosition(pos, size):
    return (pos[0]*size) + pos[1]


def moveRover(n, m, commands):
    currPos = [0, 0]
    for i in commands:
        currPos = processCommand(currPos, i)

    return convertPosition(currPos, n)


print(moveRover(4, 6, commands=[
      "RIGHT", "DOWN", "LEFT", "LEFT", "DOWN"]))
