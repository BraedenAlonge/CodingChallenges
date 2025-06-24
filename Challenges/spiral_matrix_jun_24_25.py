import numpy as np

def spiral(matrix, direction=0):
    x = [0, matrix.shape[1]]
    y = [0, matrix.shape[0]]
    output = []
    while len(output) != matrix.size:

        if direction == 0: # Right
            for i in range(x[0], x[1]):
                output.append(matrix[y[0]][i].item()) # Keep row, iterate across
            x[1] = x[1] - 1
            y[0] = y[0] + 1
            direction = 1

        elif direction == 1: # Down
            for i in range(y[0], y[1]):
                output.append(matrix[i][x[1]].item())  # Move row down, keep last unused col
            y[1] = y[1] - 1

            direction = 2

        elif direction == 2: # Left
            for i in range(x[1] - 1,x[0] - 1,-1):
                output.append(matrix[y[1]][i].item())

            direction = 3
        else: # Up
            for i in range(y[1] - 1,y[0] - 1,-1):
                output.append(matrix[i][x[0]].item())
            x[0] = x[0] + 1
            direction = 0

    return output